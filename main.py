from random import randrange

a = randrange(100)

print("Zagrajmy w grę - wylosowałem jakąś liczbę, twoim zadaniem będzie zgadnąć co to za liczba. Mało ekscytujące? No nic nie poradzę, kazdy sie kiedyś uczył. Zaczynaj!")

while True:
    n = int(input())
    
    if a == n:
        break
    
    if a > n:
        print("Twoja liczba jest za mała")
    else:
        print("Twoja liczba jest za duża")

print("Udało ci się!")
