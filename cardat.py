def cardAt(n):
    """
    this function can find the card that by int n(the number of position of the card)
    and return with signature if card like 3C,5H,AS with string
    >>> cardAt(35)
    'JH'
    >>> cardAt(34)
    '0H' 
    >>> cardAt(0)
    '2c'
    >>> cardAt(-1)
    ValueError
    >>> cardAt("n")
    TypeError
    >>> cardAt(0.1)
    TypeError

    """
    if type(n) != type(1):
        raise TypeError("Not a number")
    if  n >= 52 or n < 0:
        raise ValueError("Out of Card")

    numcard = ["2", "3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A"]
    signature = ["C", "D", "H", "S"]
    PosOfNumcard = (n) % 13
    print(PosOfNumcard)
    PosOfSignature = (n) // 13
    card = numcard[PosOfNumcard] + signature[PosOfSignature]
    return card
