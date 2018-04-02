GAME = [
    10, # strike, add next 2 balls
    3, 7, # spare, add next ball
    6, 1,
    10, # strike, add next 2 balls
    10, # strike, add next 2 balls
    10, # strike, add next 2 balls
    2, 8, # spare, add next ball
    9, 0,
    7, 3, # spare, add next ball
    10, 10, 10, # last frame strike, 2 extra balls
    # 2, 8, 10, # last frame spare, extra ball
    # 1, 2, # last frame
]


def get_frames(game):
    frames = {}
    current_frame_index = 1
    current_ball_index = 0

    while current_ball_index < len(game):

        ball_1 = game[current_ball_index]

        if current_frame_index == 10: # last frame
            ball_2 = game[current_ball_index + 1]
            balls = ball_1 + ball_2

            frames[current_frame_index] = [ball_1, ball_2]

            if ball_1 == 10 or balls == 10: # strike or spare
                ball_3 = game[current_ball_index + 2]
                frames[current_frame_index].append(ball_3)

            current_ball_index += 2
        else:
            if ball_1 == 10: # strike
                frames[current_frame_index] = [ball_1]
                current_frame_index += 1
            else:
                ball_2 = game[current_ball_index + 1]
                balls = ball_1 + ball_2

                if balls <= 10: # spare
                    frames[current_frame_index] = [ball_1, ball_2]
                    current_ball_index += 1
                else:
                    frames[current_frame_index] = [ball_1]

                current_frame_index += 1

        current_ball_index += 1

    return frames

def get_score(game, frames):
    score = 0
    j = 0 # global game index

    for i in frames:
        frame = frames[i]

        if len(frame) == 1: # strike
            score += frame[0] + game[j+1] + game[j+2]
        else:
            points = frame[0] + frame[1]

            if i == 10 and points >= 10: # last frame strike or spare
                points += frame[2]

            score += points
            if points == 10: # spare
                score += game[j+2]
            j += 1

        j += 1
        print i, '-', frame, '=', score

    return score

def main():
    frames = get_frames(GAME)
    score = get_score(GAME, frames)

    print '\nscore:', score

if __name__ == '__main__':
    main()
