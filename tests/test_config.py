import json
import unittest
from pathlib import Path

from src.config import config, ConfigWatcher
from src.enums import Desktop, Modes, PluginKey

config_path = f"{Path.home()}/.config/yin_yang/yin_yang_dev.json"

old_configs = {
    2.1: {
        "version": 2.1,
        "desktop": "kde",
        "followSun": False,
        "latitude": "",
        "longitude": "",
        "schedule": True,
        "switchToDark": "20:0",
        "switchToLight": "7:0",
        "running": False,
        "theme": "",
        "codeLightTheme": "Default Light+",
        "codeDarkTheme": "Default Dark+",
        "codeEnabled": False,
        "kdeLightTheme": "org.kde.breeze.desktop",
        "kdeDarkTheme": "org.kde.breezedark.desktop",
        "kdeEnabled": False,
        "gtkLightTheme": "",
        "gtkDarkTheme": "",
        "atomLightTheme": "",
        "atomDarkTheme": "",
        "atomEnabled": False,
        "gtkEnabled": False,
        "wallpaperLightTheme": "",
        "wallpaperDarkTheme": "",
        "wallpaperEnabled": False,
        "firefoxEnabled": False,
        "firefoxDarkTheme": "firefox-compact-dark@mozilla.org",
        "firefoxLightTheme": "firefox-compact-light@mozilla.org",
        "firefoxActiveTheme": "firefox-compact-light@mozilla.org",
        "gnomeEnabled": False,
        "gnomeLightTheme": "",
        "gnomeDarkTheme": "",
        "kvantumEnabled": False,
        "kvantumLightTheme": "",
        "kvantumDarkTheme": "",
        "soundEnabled": False
    },
    2.2: {
        "version": 2.2,
        "desktop": "kde",
        "followSun": False,
        "latitude": "",
        "longitude": "",
        "schedule": True,
        "switchToDark": "20:0",
        "switchToLight": "7:0",
        "running": False,
        "theme": "",
        "codeLightTheme": "Default Light+",
        "codeDarkTheme": "Default Dark+",
        "codeEnabled": False,
        "systemLightTheme": "org.kde.breeze.desktop",
        "systemDarkTheme": "org.kde.breezedark.desktop",
        "systemEnabled": False,
        "gtkLightTheme": "",
        "gtkDarkTheme": "",
        "atomLightTheme": "",
        "atomDarkTheme": "",
        "atomEnabled": False,
        "gtkEnabled": False,
        "wallpaperLightTheme": "",
        "wallpaperDarkTheme": "",
        "wallpaperEnabled": False,
        "firefoxEnabled": False,
        "firefoxDarkTheme": "firefox-compact-dark@mozilla.org",
        "firefoxLightTheme": "firefox-compact-light@mozilla.org",
        "firefoxActiveTheme": "firefox-compact-light@mozilla.org",
        "kvantumEnabled": False,
        "kvantumLightTheme": "",
        "kvantumDarkTheme": "",
        "soundEnabled": False
    }
}


def downgrade_config(old_config):
    with open(config_path, "w+") as file:
        json.dump(old_config, file)

    config.load()


def use_all_versions(func):
    def inner(self):
        for version in old_configs:
            with self.subTest('Testing update from old version', version=version):
                old_config = old_configs[version]
                downgrade_config(old_config)
                func(self, version, old_config)

    return inner


class ConfigTest(unittest.TestCase):
    @use_all_versions
    def test_update_old_configs(self, version, old_config):
        match version:
            case 2.1:
                for plugin_property in ['Enabled', 'LightTheme', 'DarkTheme']:
                    self.assertEqual(
                        old_config['wallpaper' + plugin_property],
                        config.get_plugin_key('wallpaper', plugin_property.replace('Theme', '_theme').lower()),
                        'Updating old config files should apply correct values')
            case 2.2:
                self.assertEqual(config.mode, Modes.SCHEDULED)
                self.assertEqual(old_config['wallpaperEnabled'], config.get_plugin_key('wallpaper', 'enabled'))
                self.assertEqual(old_config['wallpaperLightTheme'], config.get_plugin_key('wallpaper', 'light_theme'))

    @unittest.skipIf(config.desktop == Desktop.UNKNOWN, 'Desktop is unsupported')
    @use_all_versions
    def test_updates_system_plugin_values(self, version, old_config):
        match version:
            case 2.1:
                for plugin_property in ['Enabled', 'LightTheme', 'DarkTheme']:
                    self.assertEqual(
                        old_config['wallpaper' + plugin_property],
                        config.get_plugin_key('wallpaper', plugin_property.replace('Theme', '_theme').lower()),
                        'Updating old config files should apply correct values')

            case 2.2:
                self.assertEqual(config.mode, Modes.SCHEDULED)
                self.assertEqual(old_config['wallpaperEnabled'], config.get_plugin_key('wallpaper', 'enabled'))
                self.assertEqual(old_config['wallpaperLightTheme'], config.get_plugin_key('wallpaper', 'light_theme'))

    def test_notifies_on_change(self):
        config.reset()

        class Watcher(ConfigWatcher):
            def __init__(self):
                self.updates: [(str, any, any, str)] = []

            def notify(self, key, old, new, plugin=None):
                self.updates.append((key, old, new, plugin))

        watcher = Watcher()
        config.add_update_listener(watcher)

        config.mode = Modes.SCHEDULED
        self.assertTrue(('mode', Modes.MANUAL.value, Modes.SCHEDULED.value, None) in watcher.updates)
        watcher.updates = []

        config.mode = Modes.SCHEDULED
        self.assertFalse(('mode', Modes.MANUAL.value, Modes.SCHEDULED.value, None) in watcher.updates)
        watcher.updates = []

        config.update_plugin_key('wallpaper', PluginKey.ENABLED, True)
        self.assertTrue(('enabled', False, True, 'wallpaper') in watcher.updates)
        watcher.updates = []

        try:
            config.update_plugin_key('abcd', PluginKey.ENABLED, True)
        except KeyError:
            pass
        self.assertTrue(len(watcher.updates) == 0)

    def test_write_when_changed(self):
        config.reset()
        config.save()
        self.assertFalse(config.save())

        config.mode = Modes.SCHEDULED
        self.assertTrue(config.save())

        config.update_plugin_key('wallpaper', PluginKey.ENABLED, True)
        self.assertTrue(config.save())


if __name__ == '__main__':
    unittest.main()
