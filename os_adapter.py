import abc
import os
from abc import abstractmethod


class OSAdapter(abc.ABC):
    @abstractmethod
    def lock_screen(self):
        raise NotImplementedError()

    @abstractmethod
    def open_yubikey_auth(self):
        raise NotImplementedError()

    @abstractmethod
    def set_max_brightness(self):
        raise NotImplementedError()

    @abstractmethod
    def copy(self):
        raise NotImplementedError()

    @abstractmethod
    def paste(self):
        raise NotImplementedError()

    @abstractmethod
    def select_all(self):
        raise NotImplementedError()

    @abstractmethod
    def volume_up(self):
        raise NotImplementedError()

    @abstractmethod
    def volume_down(self):
        raise NotImplementedError()

    @abstractmethod
    def next_browser_tab(self):
        raise NotImplementedError()

    def tell(self, text: str):
        pass


class SpecialFeaturesMixin:
    @abstractmethod
    def open_in_browser(self, url: str):
        raise NotImplementedError()

    def open_daily(self):
        try:
            with open("daily_url.txt", "r") as f:
                url = f.readline()
                if url.startswith("https://"):
                    self.open_in_browser(url)
        except:
            print("Error opening daily in browser")


class MacOSAdapter(OSAdapter, SpecialFeaturesMixin):
    def lock_screen(self):
        os.system("pmset displaysleepnow")

    def open_yubikey_auth(self):
        os.system("open /Applications/Yubico\ Authenticator.app")

    def set_max_brightness(self):
        for _ in range(16):
            os.system(
                "osascript -e 'tell application \"System Events\"' -e 'key code 144' -e ' end tell'"
            )

    def copy(self):
        os.system(
            'osascript -e \'tell application "System Events" to keystroke "c" using {command down}\''
        )

    def paste(self):
        os.system(
            'osascript -e \'tell application "System Events" to keystroke "v" using {command down}\''
        )

    def select_all(self):
        os.system(
            'osascript -e \'tell application "System Events" to keystroke "a" using {command down}\''
        )

    def volume_up(self):
        os.system(
            'osascript -e "set volume output volume (get output volume of (get volume settings) + 15)"'
        )

    def volume_down(self):
        os.system(
            'osascript -e "set volume output volume (get output volume of (get volume settings) - 15)"'
        )

    def next_browser_tab(self):
        os.system(
            'osascript -e \'tell application "System Events" to keystroke "tab" using {contol down}\''
        )

    def tell(self, text: str):
        os.system('say "Экран заблокирован"')

    def open_in_browser(self, url: str):
        os.system("open " + url)
