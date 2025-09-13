from rich.console import Console

console=Console()

name = None
balance = None

def open_account():
    global name, balance
    name = console.input("[yellow]name = [/yellow]")
    balance = 0.0

def check_account():
    return name is not None and balance is not None

def deposit():
    global balance
    amount = float(console.input("[blue]Qo'shiladigan summani kiriting: [/blue]"))
    balance += amount

def withdraw():
    global balance
    amount = float(console.input("[blue]Yechiladigan summani kiriting: [/blue]"))
    balance -= amount

def check_balance():
    print(f"Hozirgi balans: {balance} so'm")

def main():
    while True:
        console.print("[green]\n===== Menyu =====[/green]")
        console.print("[green]0 - Account yaratish[/green]")
        console.print("[green]1 - Balansni ko'rish[/green]")
        console.print("[green]2 - Pul qo'shish (deposit)[/green]")
        console.print("[green]3 - Pul yechish (withdraw)[/green]")
        console.print("[red]4 - Chiqish[/red]")

        tanlov = console.input("[yellow]Amalni tanlang (0-4): [/yellow]")

        if tanlov == "0":
            open_account()
        elif tanlov == "1":
            if check_account():
                check_balance()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "2":
            if check_account():
                deposit()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "3":
            if check_account():
                withdraw()
            else:
                print("Iltimos, avval account yarating.")
                open_account()
        elif tanlov == "4":
            console.print("[red]Dasturdan chiqildi. Xayr![/red]")
            break
        else:
            console.print("[red]Noto'g'ri tanlov! Iltimos, qaytadan urinib ko'ring.[/red]")
main()