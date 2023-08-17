def get_chord(info):
    chord = []
    stack = ''
    for i in info:
        if chr(96) < i.lower() < chr(123) and stack == '':
            stack += i
        elif chr(96) < i.lower() < chr(123) and stack != '':
            chord.append(stack)
            stack = i
        else:
            stack += i
    chord.append(stack)

    return chord


def solution(m, musicinfos):
    answer = []
    m = get_chord(m)
    length = len(musicinfos)
    ml = len(m)

    new_music_infos = []

    for i in range(length):
        music_info = musicinfos[i].split(',')
        start = list(map(int, music_info[0].split(':')))
        end = list(map(int, music_info[1].split(':')))
        music_playtime = abs((end[0] * 60 + end[1]) - (start[0] * 60 + start[1]))

        music_name = music_info[2]
        music_chord = get_chord(music_info[3])
        music_playchord = music_chord * (music_playtime // len(music_chord)) + music_chord[:music_playtime % len(music_chord)]

        new_music_infos.append([music_playtime, i + 1, music_name, music_playchord])

    for pt, idx, name, chord in new_music_infos:
        for j in range(len(chord) - ml + 1):
            if chord[j:j + ml] == m:
                answer.append((pt, idx, name))

    answer.sort(key=lambda x: (-x[0], x[1]))

    if len(answer) == 0:
        return "(None)"

    return answer[0][2]