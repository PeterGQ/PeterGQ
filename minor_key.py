if __name__ == '__main__':
    def minor_key():
        Bool = False
        Music = ['D\u266d', 'E\u266d', 'G\u266d', 'A\u266d', 'B\u266d']
        music_notes = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']
        user_input = input("Enter a starting note (C, D flat): ")
        while(user_input != "quit"):
            List = list()
            List_2 = list()
            List_3 = []
            List_4 = list()
            if (user_input[0] in music_notes) and ("flat" in user_input):# checks if input for flat exists in the music_notes list.
                flat = user_input[0] + "\u266d"
                w = music_notes.index(flat)
                List.append(music_notes[:w])
                List_2.append(music_notes[w:])
                z = List[0]
                h = " ".join(z).strip("[]")
                x = List_2[0]
                j = " ".join(x).strip("[]")
                List_3 = (j + " " + h).split(" ")
                List_4.append(List_3[0])
                List_4.append(List_3[2])
                List_4.append(List_3[3])
                List_4.append(List_3[5])
                List_4.append(List_3[7])
                List_4.append(List_3[8])
                List_4.append(List_3[11])
                List_4.append(List_3[0])
                k = str(List_4).strip()
                print(" ".join(List_4))

            elif(user_input in music_notes):
                w = music_notes.index(user_input)
                List.append(music_notes[:w])
                List_2.append(music_notes[w:])
                z = List[0]
                h = " ".join(z).strip("[]")
                x = List_2[0]
                j = " ".join(x).strip("[]")
                List_3 = (j + " " + h).split(" ")
                List_4.append(List_3[0])
                List_4.append(List_3[2])
                List_4.append(List_3[3])
                List_4.append(List_3[5])
                List_4.append(List_3[7])
                List_4.append(List_3[8])
                List_4.append(List_3[11])
                List_4.append(List_3[0])
                k = str(List_4).strip()
                print(" ".join(List_4))

            else:
