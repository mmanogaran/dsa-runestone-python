import random
import string

"""
Here’s a self check that really covers everything so far. You may have heard of
the infinite monkey theorem? The theorem states that a monkey hitting keys at
random on a typewriter keyboard for an infinite amount of time will almost
surely type a given text, such as the complete works of William Shakespeare.
Well, suppose we replace a monkey with a Python function. How long do you think
it would take for a Python function to generate just one sentence of
Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”.

You’re not going to want to run this one in the browser, so fire up your
favorite Python IDE. The way we’ll simulate this is to write a function that
generates a string that is 28 characters long by choosing random letters from
the 26 letters in the alphabet plus the space. We’ll write another function
that will score each generated string by comparing the randomly generated string
to the goal.

A third function will repeatedly call generate and score, then if 100% of the
letters are correct we are done. If the letters are not correct then we will
generate a whole new string.To make it easier to follow your program’s progress
this third function should print out the best string generated so far and its
score every 1000 tries.
"""


def rand_string(len):
    """Return a random string of length len.

    Args:
        len (int): desired length of random string

    Returns:
        str: random string of length len
    """
    return "".join(random.choices(string.ascii_lowercase + " ", k=len))


def comp_string(string, goal):
    """Compare string with goal and returns percentage score according to how
    many characters they share in the same index.

    Args:
        string (str): A string of length n
        goal (str): A string of length n

    Returns:
        float: A percentage score of how similar stringis to goal
    """
    length = len(string)
    matches = 0

    for i in range(length):

        if string[i] == goal[i]:
            matches += 1

    return matches / length


def rand_gen_and_score(goal, num_attempts=1000000):
    """Return when it generates a random string that matches goal, on the
    'num_attempts'th try, or when the program is interrupted by the user. Prints
    best strings generated.

    Args:
        goal (str): Goal string to generate
        num_attempts (int, optional): Number of times to try and generate goal.
                                      Defaults to 1000000.
    """
    try:
        count = 0
        best_str = ""
        best_score = 0

        while True:
            rand_str = rand_string(len(goal))
            score = comp_string(rand_str, goal)

            if score == 100:
                print("Got it on {}th try: {}".format(count, rand_str))
                return
            elif score > best_score:
                best_score = score
                best_str = rand_str
                print(
                    "Best String: {} with score {} on {}th try".format(
                        best_str, best_score, count
                    )
                )

            count += 1

            if count == num_attempts:
                print("Tried {} times. Stopping.".format(num_attempts))
                return

    except KeyboardInterrupt:
        pass


"""
See if you can improve upon the program in the self check by keeping letters
that are correct and only modifying one character in the best string so far.
This is a type of algorithm in the class of ‘hill climbing’ algorithms, that is
we only keep the result if it is better than the previous one.
"""


def climbing_gen_and_score(goal):
    """Generate a random string and randomly modify one character at a time
    until it matches goal.

    Args:
        goal (str): Goal string to generate
    """
    best_str = rand_string(len(goal))
    best_score = comp_string(best_str, goal)
    count = 0
    i = 0

    while best_score != 1:

        if best_str[i] == goal[i]:
            i += 1

        new_str = list(best_str)
        new_str[i] = "".join(random.choices(string.ascii_lowercase + " "))
        new_score = comp_string(new_str, goal)

        if new_score > best_score:
            best_score = new_score
            best_str = "".join(new_str)
            print(
                "Climbed on {}th try to '{}' with {}".format(
                    count, best_str, best_score
                )
            )

        count += 1

    print("Got it on {}th try!".format(count - 1))
    return


if __name__ == "__main__":
    goal = "methinks it is like a weasel"
    rand_gen_and_score(goal)
    climbing_gen_and_score(goal)
