def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def affine_decrypt(encrypted, key, mod, alphabet):
    text = ''
    for c in encrypted:
        a = modinv(key[0], mod)
        index = ((a*int(c)+a*(-key[1]))%mod)
        text += alphabet[index]
    return text

def main():
    key = [66, 38]
    mod = 97
    alphabet = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','~','!','@','#','$','%','^','&','*','(',')','_','+','`','1','2','3','4','5','6','7','8','9','0','-','=','<','>','?',':','"','{','}','|',',','.','/','\'','[',']','\\','\t',' ','\n',';')
    to_decryption = list(map(int, input().split()))
    #example encrypted text
    '''to_decryption = [31, 59, 34, 74, 78, 88, 34, 59, 63, 34, 90, 59, 1, 34, 1, 59, 34, 74, 78, 88, 34, 1, 82, 8, 1, 34, 51, 32, 34, 1, 82, 78, 34, 94, 67, 78, 32, 1, 51, 59, 90, 49, 3, 35, 82, 78, 1, 82, 78, 63, 34, 92, 1, 51, 32, 34, 90, 59, 74, 55, 78, 63, 34, 51, 90, 34, 1, 82, 78, 34, 24, 51, 90, 12, 34, 1, 59, 34, 32, 67, 47, 47, 78, 63, 3, 31, 82, 78, 34, 32, 55, 51, 90, 16, 32, 34, 8, 90, 12, 34, 8, 63, 63, 59, 5, 32, 34, 59, 47, 34, 59, 67, 1, 63, 8, 16, 78, 59, 67, 32, 34, 47, 59, 63, 1, 67, 90, 78, 88, 3, 89, 63, 34, 1, 59, 34, 1, 8, 86, 78, 34, 8, 63, 24, 32, 34, 8, 16, 8, 51, 90, 32, 1, 34, 8, 34, 32, 78, 8, 34, 59, 47, 34, 1, 63, 59, 67, 74, 55, 78, 32, 3, 38, 90, 12, 34, 74, 40, 34, 59, 28, 28, 59, 32, 51, 90, 16, 34, 78, 90, 12, 34, 1, 82, 78, 24, 57, 34, 31, 59, 34, 12, 51, 78, 1, 59, 34, 32, 55, 78, 78, 28, 88, 3, 23, 59, 34, 24, 59, 63, 78, 69, 34, 8, 90, 12, 34, 74, 40, 34, 8, 34, 32, 55, 78, 78, 28, 34, 1, 59, 34, 32, 8, 40, 34, 5, 78, 34, 78, 90, 12, 3, 31, 82, 78, 34, 82, 78, 8, 63, 1, 10, 8, 43, 82, 78, 34, 8, 90, 12, 34, 1, 82, 78, 34, 1, 82, 59, 67, 32, 8, 90, 12, 34, 90, 8, 1, 67, 63, 8, 55, 34, 32, 82, 59, 43, 86, 32, 3, 31, 82, 8, 1, 34, 47, 55, 78, 32, 82, 34, 51, 32, 34, 82, 78, 51, 63, 34, 1, 59, 49, 34, 92, 1, 51, 32, 34, 8, 34, 43, 59, 90, 32, 67, 24, 24, 8, 1, 51, 59, 90, 3, 42, 78, 36, 59, 67, 1, 55, 40, 34, 1, 59, 34, 74, 78, 34, 5, 51, 32, 82, 92, 12, 57, 34, 31, 59, 34, 12, 51, 78, 88, 34, 1, 59, 34, 32, 55, 78, 78, 28, 69, 3, 31, 59, 34, 32, 55, 78, 78, 28, 88, 34, 28, 78, 63, 43, 82, 8, 90, 43, 78, 34, 1, 59, 34, 12, 63, 78, 8, 24, 8, 40, 88, 34, 1, 82, 78, 63, 78, 92, 32, 34, 1, 82, 78, 34, 63, 67, 74, 49, 3, 77, 59, 63, 34, 51, 90, 34, 1, 82, 8, 1, 34, 32, 55, 78, 78, 28, 34, 59, 47, 34, 12, 78, 8, 1, 82, 34, 5, 82, 8, 1, 34, 12, 63, 78, 8, 24, 32, 34, 24, 8, 40, 34, 43, 59, 24, 78, 88, 3, 35, 82, 78, 90, 34, 5, 78, 34, 82, 8, 36, 78, 34, 32, 82, 67, 47, 47, 55, 78, 12, 34, 59, 47, 47, 34, 1, 82, 51, 32, 34, 24, 59, 63, 1, 8, 55, 34, 43, 59, 51, 55, 88, 3, 54, 67, 32, 1, 34, 16, 51, 36, 78, 34, 67, 32, 34, 28, 8, 67, 32, 78, 1, 82, 78, 63, 78, 92, 32, 34, 1, 82, 78, 34, 63, 78, 32, 28, 78, 43, 1, 3, 31, 82, 8, 1, 34, 24, 8, 86, 78, 32, 34, 43, 8, 55, 8, 24, 51, 1, 40, 34, 59, 47, 34, 32, 59, 34, 55, 59, 90, 16, 34, 55, 51, 47, 78, 57, 3, 77, 59, 63, 34, 5, 82, 59, 34, 5, 59, 67, 55, 12, 34, 74, 78, 8, 63, 34, 1, 82, 78, 34, 5, 82, 51, 28, 32, 34, 8, 90, 12, 34, 32, 43, 59, 63, 90, 32, 34, 59, 47, 34, 1, 51, 24, 78, 88, 3, 31, 82, 92, 59, 28, 28, 63, 78, 32, 32, 59, 63, 92, 32, 34, 5, 63, 59, 90, 16, 88, 34, 1, 82, 78, 34, 28, 63, 59, 67, 12, 34, 24, 8, 90, 92, 32, 34, 43, 59, 90, 1, 67, 24, 78, 55, 40, 88, 3, 31, 82, 78, 34, 28, 8, 90, 16, 32, 34, 59, 47, 34, 12, 51, 32, 28, 63, 51, 9, 92, 12, 34, 55, 59, 36, 78, 88, 34, 1, 82, 78, 34, 55, 8, 5, 92, 32, 34, 12, 78, 55, 8, 40, 88, 3, 31, 82, 78, 34, 51, 90, 32, 59, 55, 78, 90, 43, 78, 34, 59, 47, 34, 59, 47, 47, 51, 43, 78, 88, 34, 8, 90, 12, 34, 1, 82, 78, 34, 32, 28, 67, 63, 90, 32, 3, 31, 82, 8, 1, 34, 28, 8, 1, 51, 78, 90, 1, 34, 24, 78, 63, 51, 1, 34, 59, 47, 34, 1, 82, 92, 67, 90, 5, 59, 63, 1, 82, 40, 34, 1, 8, 86, 78, 32, 88, 3, 35, 82, 78, 90, 34, 82, 78, 34, 82, 51, 24, 32, 78, 55, 47, 34, 24, 51, 16, 82, 1, 34, 82, 51, 32, 34, 94, 67, 51, 78, 1, 67, 32, 34, 24, 8, 86, 78, 3, 35, 51, 1, 82, 34, 8, 34, 74, 8, 63, 78, 34, 74, 59, 12, 86, 51, 90, 80, 34, 35, 82, 59, 34, 5, 59, 67, 55, 12, 34, 47, 8, 63, 12, 78, 55, 32, 34, 74, 78, 8, 63, 88, 3, 31, 59, 34, 16, 63, 67, 90, 1, 34, 8, 90, 12, 34, 32, 5, 78, 8, 1, 34, 67, 90, 12, 78, 63, 34,
8, 34, 5, 78, 8, 63, 40, 34, 55, 51, 47, 78, 88, 3, 7, 67, 1, 34, 1, 82, 8, 1, 34, 1, 82, 78, 34, 12, 63, 78, 8, 12, 34, 59, 47, 34, 32, 59, 24, 78, 1, 82, 51, 90, 16, 34, 8, 47, 1, 78, 63, 34, 12, 78, 8, 1, 82, 88, 3, 31, 82, 78, 34, 67, 90, 12, 51, 32, 43, 59, 36, 78, 63, 78, 92, 12, 34, 43, 59, 67, 90, 1, 63, 40, 88, 34, 47, 63, 59, 24, 34, 5, 82, 59, 32, 78, 34, 74, 59, 67, 63, 90, 3, 23, 59, 34, 1, 63, 8, 36, 78, 55, 55, 78, 63, 34, 63, 78, 1, 67, 63, 90, 32, 88, 34, 28, 67, 9, 9, 55, 78, 32, 34, 1, 82, 78, 34, 5, 51, 55, 55, 88, 3, 38, 90, 12, 34, 24, 8, 86, 78, 32, 34, 67, 32, 34, 63, 8, 1, 82, 78, 63, 34, 74, 78, 8, 63, 34, 1, 82, 59, 32, 78, 34, 51, 55, 55, 32, 34, 5, 78, 34, 82, 8, 36, 78, 3, 31, 82, 8, 90, 34, 47, 55, 40, 34, 1, 59, 34, 59, 1, 82, 78, 63, 32, 34, 1, 82, 8, 1, 34, 5, 78, 34, 86, 90, 59, 5, 34, 90, 59, 1, 34, 59, 47, 80, 3, 31, 82, 67, 32, 34, 43, 59, 90, 32, 43, 51, 78, 90, 43, 78, 34, 12, 59, 78, 32, 34, 24, 8, 86, 78, 34, 43, 59, 5, 8, 63, 12, 32, 34, 59, 47, 34, 67, 32, 34, 8, 55, 55, 88, 3, 38, 90, 12, 34, 1, 82, 67, 32, 34, 1, 82, 78, 34, 90, 8, 1, 51, 36, 78, 34, 82, 67, 78, 34, 59, 47, 34, 63, 78, 32, 59, 55, 67, 1, 51, 59, 90, 3, 81, 32, 34, 32, 51, 43, 86, 55, 51, 78, 12, 34, 59, 92, 78, 63, 34, 5, 51, 1, 82, 34, 1, 82, 78, 34, 28, 8, 55, 78, 34, 43, 8, 32, 1, 34, 59, 47, 34, 1, 82, 59, 67, 16, 82, 1, 88, 3, 38, 90, 12, 34, 78, 90, 1, 78, 63, 28, 63, 51, 32, 78, 32, 34, 59, 47, 34, 16, 63, 78, 8, 1, 34, 28, 51, 1, 43, 82, 34, 8, 90, 12, 34, 24, 59, 24, 78, 90, 1, 3, 35, 51, 1, 82, 34, 1, 82, 51, 32, 34, 63, 78, 16, 8, 63, 12, 34, 1, 82, 78, 51, 63, 34, 43, 67, 63, 63, 78, 90, 1, 32, 34, 1, 67, 63, 90, 34, 8, 5, 63, 40, 3, 38, 90, 12, 34, 55, 59, 32, 78, 34, 1, 82, 78, 34, 90, 8, 24, 78, 34, 59, 47, 34, 8, 43, 1, 51, 59, 90, 57, 3]
'''
    print('Decrypted Text: {}'.format(affine_decrypt(to_decryption, key, mod, alphabet)))

if __name__ == '__main__':
    main()
