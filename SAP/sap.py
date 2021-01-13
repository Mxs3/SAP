from pydub import AudioSegment
from pydub.playback import play
import colorama as color 
from colorama import Fore
import sys

def play_audio():
    print(f"{Fore.BLUE}Please enter file path or type 'c' to exit: ")
    while True:
        try:
            file_path = input()
            if file_path == 'c':
                print(f'{Fore.RED}Exiting...\n')
                sys.exit()
            else:
                pass
            audio_file = AudioSegment.from_file(file_path)
            print(f'{Fore.GREEN}PLaying audio file at: ...' + str(file_path) + '\n')
            play(audio_file)
        except KeyboardInterrupt as kb:
            print(f'\n{Fore.RED}Stopped audio\n' + str(kb) + '\n')
            play_audio()

print(f'{Fore.RED} ----------------------------------')
print(f'{Fore.BLUE}|                                |')
print(f'{Fore.BLUE}|         Welcome to SAP         |')
print(f'{Fore.BLUE}|                                |')
print(f'{Fore.RED} ----------------------------------')
play_audio()
