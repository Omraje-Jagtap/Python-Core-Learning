'''Task:

 - Given  pairs of names and email addresses as input, 
   print each name and email address pair having a valid email address on a new line.

A valid email address meets the following criteria:

 - It's composed of a username, domain name, and extension assembled in 
   this format: username@domain.extension

 - The username starts with an English alphabetical character, 
   and any subsequent characters consist of one or more of the following: 
   alphanumeric characters, -,., and _.

 - The domain and extension contain only English alphabetical characters.

 - The extension is 1,2, or 3 characters in length.

Input Format:

 - The first line contains a single integer, n , denoting the number of email address.
 - Each line i of the n subsequent lines contains a name and an email address as 
   two space-separated values following this format: name <user@email.com>

Constraints:

 - 0 < N < 100

Output Format:

 - Print the space-separated name and email address pairs containing valid email addresses only. 
   Each pair must be printed on a new line in the following format: name <user@email.com>

 - You must print each valid email address in the same order as it was received as input.

Sample Input:

2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>

Sample Output:

DEXTER <dexter@hotmail.com>

Explanation:

 - dexter@hotmail.com is a valid email address, so we print the name and 
   email address pair received as input on a new line.
 - virus!@variable.:p is not a valid email address because the username contains 
   an exclamation point (!) and the extension 
   contains a colon (:). As this email is not valid, we print nothing.
   
'''


def check_email(emails, n):

    if 0 < n < 100:
        valid_emails = []

        for i in range(n):
            raw_email = emails[i][1]
            email = raw_email.strip("<>") 

            check = True

            if '@' not in email:
                check = False

            elif not email[0].isalpha():
                check = False

            else:

                domain_start_idx = email.find('@') + 1
                last_occurence_dot = email.rfind('.')

                if last_occurence_dot == -1:
                    check = False
                else:
                    domains = email[domain_start_idx:last_occurence_dot]
                    extension = email[last_occurence_dot+1:]

                    if not domains.isalpha():
                        check = False

                    elif not (0 < len(extension) < 5 and extension.isalpha()):
                        check = False

                    local = email[:email.find('@')]
                    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._")
                    if not all(ch in allowed for ch in local):
                        check = False

            if check:
                valid_emails.append(f"{emails[i][0]} <{email}>")

        return valid_emails


N = int(input())
name_emails = []

for i in range(N):
    user_name_mails = input().split()
    name_emails.append(user_name_mails)

result = check_email(name_emails, N)

for i in result:
    print(i)

