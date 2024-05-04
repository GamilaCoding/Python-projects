secter_word = "your country"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

while guess !=secter_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("enter guess")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print(" You lose out of guesses")
else:
    print("You Win")