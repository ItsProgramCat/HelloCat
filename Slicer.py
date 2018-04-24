#get user email address

email = input("what is your email address?: ").strip()

#slice out username

user = email[:email.index("@")]

#slice out domain name

domain = email[email.index("@") + 1: ]

#format message

output = "Your username is {} and your domain is {}".format(user,domain)


#display output message
print(output)
