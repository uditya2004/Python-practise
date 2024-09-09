def check_pal(n, str, low):
    if low>=n//2:
        return True
    else:
        if str[low] != str[n-low-1]:
            return False
        
        return check_pal(n, str, low + 1)


str1 = "ABCDCBA"
print(check_pal(len(str1), str1, 0))