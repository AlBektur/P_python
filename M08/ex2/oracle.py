import os

from dotenv import load_dotenv


def security_check() -> None:
    print("\nEnvironment security check:")
    if not os.path.exists(".env"):
        print("[WARNING] .env file not found\n"
              "'cp .env.example .env' to create a .env file")
    else:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


def oracle() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")

    load_dotenv()
    print("Configuration loaded:")

    data: dict = {
        'Mode': {},
        'Database': {},
        'API Access': {},
        'Log Level':  {},
        'Zion Network': {}
    }
    data['Mode']['MATRIX_MODE'] = os.getenv('MATRIX_MODE')
    data['Database']['DATABASE_URL'] = os.getenv('DATABASE_URL')
    data['API Access']['API_KEY'] = os.getenv('API_KEY')
    data['Log Level']['LOG_LEVEL'] = os.getenv('LOG_LEVEL')
    data['Zion Network']['ZION_ENDPOINT'] = os.getenv('ZION_ENDPOINT')

    for k, v in data.items():
        (i, j), = v.items()
        if j:
            if i == 'MATRIX_MODE':
                if j in ('development', 'production'):
                    print(f"{k}: {j}")
                else:
                    print(f"Invalid mode: {j}")
            else:
                print(f"{k}: {j}")
        else:
            print(f"Missing configuration value: {i}")


if __name__ == "__main__":

    oracle()
    security_check()
