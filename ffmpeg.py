import subprocess
import sys

def check_ffmpeg_installed():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def install_ffmpeg_with_winget():
    subprocess.run(["winget", "install", "FFmpeg"], capture_output=True)

def main():
    # Check if FFmpeg is installed
    if not check_ffmpeg_installed():
        print("FFmpeg non è installato (che primitivo...). Uso winget per scaricare l'ultima versione magicamente...")

        try:
            install_ffmpeg_with_winget()
            if check_ffmpeg_installed():
                print("Ho installato FFmpeg! Incredibile!.")
            else:
                print("Non son riuscito ad installere FFmpeg. Ho paura che ti attacchi al cazzo...")
                sys.exit(1)
        except Exception as e:
            print("Porcozzio qualcosa è andato a troie male:", str(e))
            sys.exit(1)
    else:
        print("FFmpeg è già installato sul tuo pc... non mi rompere il cazzo...")

    # Continue with the rest of your code...

if __name__ == "__main__":
    main()
