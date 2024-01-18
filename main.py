import mysql.connector

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'SidharthPriyu',
    'database': 'GAME'
}


def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("Think of a range for the number (e.g., 1-100).")
    min_range, max_range = map(int, input(
        "Enter the minimum and maximum numbers separated by a space: ").split())
    secret_number = int(input(f"I'm thinking of a number between {
                        min_range} and {max_range}. Guess: "))
    attempts = 1

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {
                  attempts} attempts!")
            save_score(attempts)
            play_again = input("Do you want to play again (Y/N): ")
            if play_again.upper() == 'Y':
                guess_the_number()
            else:
                break


def save_score(attempts):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        username = input("Enter your username: ")
        cursor.execute(
            "INSERT INTO user_scores (username, score) VALUES (%s, %s)", (username, attempts))
        conn.commit()

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()


if __name__ == "__main__":
    guess_the_number()
