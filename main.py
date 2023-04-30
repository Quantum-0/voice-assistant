#!/usr/bin/env python
import datetime

from pocketsphinx import LiveSpeech, get_model_path
import os

import os_adapter


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))

    speech = LiveSpeech(
        verbose=False,
        hmm=get_model_path(os.path.join(current_dir, "ru")),  # directory with files:
        # feat.params feature_transform mdef means mixture_weights noisedict transition_matrices variances
        lm=get_model_path(os.path.join(current_dir, "ru.lm")),
        dic=get_model_path(os.path.join(current_dir, "ru.dic")),
    )

    adapter = os_adapter.MacOSAdapter()

    enabled = True

    adapter.tell("Голосовое управление включено")

    for phrase in speech:
        phrase = str(phrase)
        if not phrase:
            continue

        print("[" + str(datetime.datetime.now()) + "]:", phrase, end="")

        if (
            "отключить голосовое управление" in phrase
            or "выключить голосовое управление" in phrase
        ):
            enabled = False
            adapter.tell("Голосовое управление отключено")
        elif "включить голосовое управление" is phrase:
            enabled = True
            adapter.tell("Голосовое управление включено")

        if not enabled:
            print(" (ignored, because disabled)")
        else:
            print("")

        if "яркость" in phrase:
            adapter.set_max_brightness()
        if "заблокировать" in phrase:
            adapter.lock_screen()
            adapter.tell("Экран заблокирован")
        if "пароль" in phrase:
            adapter.open_yubikey_auth()
        if "выделить всё" in phrase:
            adapter.select_all()
        if "копировать" in phrase:
            adapter.copy()
        if "вставить" in phrase:
            adapter.paste()
        if "громче" in phrase:
            adapter.volume_up()
        if "тише" in phrase:
            adapter.volume_down()
        if "следующая вкладка" in phrase:
            adapter.next_browser_tab()
        if "дейли" in phrase:
            adapter.open_daily()


if __name__ == "__main__":
    main()
