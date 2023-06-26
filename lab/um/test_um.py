from um import count
import sys

def main():
    try:
        test_valid()



    except ValueError:
        sys.exit(1)

def test_valid():

    assert count("um") == 1
    assert count("yum") == 0
    assert count("Um") == 1
    assert count("yummy") == 0
    assert count(" hello um, um") == 2
    assert count(" Um") == 1
    assert count("Um, thanks, um...") == 2
    assert count("Um, thanks for the album.") == 1
    assert count("um?") == 1
    assert count("Um") == 1
    assert count(" um") == 1

if __name__=='__main__':
    main()