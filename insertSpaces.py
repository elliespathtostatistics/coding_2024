def addSpaces(str, dict):
    for i in range(len(str)):

        left = str[:i+1]
        print("left", left)

        if left in dict:

            right = str[i+1:]
            print("right", right)

            if len(right) == 0:
                print("returned left", left)
                return left

            rightWithSpaces = addSpaces(right, dict)
            print("rightWithSpaces", rightWithSpaces)

            if rightWithSpaces is not None:
                print("left:", left, "rightWithSpaces", rightWithSpaces)
                return left + ' ' + rightWithSpaces

    return None

str = "bloombergisfun"
dict = ["bloom","bloomberg","is","fun"]
addSpaces(str, dict)