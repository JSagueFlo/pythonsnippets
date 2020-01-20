from hsaudiotag import auto
import os


def main():
    # 'E:\\Pro - APPs\\script_ordenar_musica\\test\\'
    d = input("Entra el directori aboslut:\n")
    d = d + "\\"
    disc = d.split('\\')[0] + '\\'

    for filename in os.listdir(d):
        print(filename)
        filepath = os.path.join(d, filename)
        # os.rename(filepath, filepath[2:])
        # print(filepath)
        myfile = auto.File(filepath)
        print(dir(myfile))
        print(myfile.artist, myfile.title)
        if filename.endswith(".mp3"):
            print('3')
            os.rename(filepath, os.path.join(
                d, myfile.artist + ' - ' + myfile.title + ".mp3"))
        elif filename.endswith(".m4a"):
            print('4a')
            os.rename(filepath, os.path.join(
                d, myfile.artist + ' - ' + myfile.title + ".m4a"))
        elif filename.endswith(".m4p"):
            print('4p')
            os.rename(filepath, os.path.join(
                d, myfile.artist + ' - ' + myfile.title + ".m4p"))

main()
