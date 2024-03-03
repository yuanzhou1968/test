class Solution:
    i = 0
    checkStr = ""
    outPutStr = ""
    # 输入
    print("请输入字符串")
    strIn = input()
    print("请输入要求k个字符")
    k = input()
    num = int(k)
    # 考虑数组长度不足k
    slen = len(strIn)
    while i < slen:
        # 字母chari与字符串checkStr对比
        chari = chr(ord(strIn[i]))
        if i <= num:
            checkStr = strIn[0:i]
        if i > num:
            checkStr = strIn[i-num:i]
        isReplace = checkStr.find(chari)
        print(isReplace)
        print(chari)
        print("------------")
        print(checkStr)
        if isReplace != -1:
            print("replce")
            outPutStr = outPutStr + '_'
        else:
            outPutStr = outPutStr + strIn[i]
        i += 1
    print(outPutStr)