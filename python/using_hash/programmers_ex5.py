def solution(genres, plays):
    answer = []
    genres_total_play_dict = dict()
    genres_play_dict = dict()
    sorted_by_play_dict = dict()
    for genre in set(genres):
        genres_play_dict[genre] = dict()

    for index, (genre, play) in enumerate(zip(genres, plays)):
        genres_total_play_dict[genre] = genres_total_play_dict.get(genre, 0) + play
        genres_play_dict[genre].update(dict({index:play}))

    for genre, genres_play in genres_play_dict.items():
        sorted_by_play_dict[genre] = get_number_list_desc_by_play_limit_2(genres_play)

    sorted_by_genre = [key for key, value in get_list_desc_by_value(genres_total_play_dict)]

    for genre in sorted_by_genre:
        answer.extend(sorted_by_play_dict[genre])
    return answer

def get_number_list_desc_by_play_limit_2(genres_play):
    sorted_by_play = list()
    for key, value in get_list_desc_by_value(genres_play):
        if len(sorted_by_play) < 2:
            sorted_by_play.append(key)
        else:
            break
    return sorted_by_play

def get_list_desc_by_value(base_dict):
    return sorted(base_dict.items(),key = lambda x: x[1], reverse=True)


def solution2(genres, plays):
    genre_count_dict = dict()
    genre_dict = dict()
    play_dict = dict()
    answer = []

    for index in range(len(genres)):
        genre_dict[index] = genres[index]
        play_dict[index] = plays[index]


    for index, genre in enumerate(genres):
        genre_dict[genre] = genre_dict.get(genre, list())
        genre_dict[genre].append(index)
        genre_count_dict[genre] = genre_count_dict.get(genre, 0)
        genre_count_dict[genre] += plays[index]
        play_dict[index] = plays[index]


    for genre, _ in sorted(genre_count_dict.items(), key=lambda x:x[1], reverse = True):
        a_dict = dict()
        for index in genre_dict[genre]:
            a_dict[index] = play_dict[index]

        for index, _ in sorted(a_dict.items(), key=lambda x:x[1], reverse=True)[:2]:
            answer.append(index)

    return answer