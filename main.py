import monetary_policy as mp

def main():
    print("Hello from lecture-7!")


if __name__ == "__main__":
    main()

# Now we just use the 'mp.' prefix
fed = mp.CentralBank(policy='active', interest_rate=0.01)
print(fed.interest_rate)


# as it is a class inside the module i need to call the module each time (other option is to import the specific module inside the class)
help(mp.CentralBank)

from monetary_policy import CentralBank
snb = CentralBank()
help(CentralBank)


print(CentralBank.__doc__)

 