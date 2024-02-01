from playwright.sync_api import sync_playwright

def main():
    try:
        with sync_playwright as p:
            browser = p.chromium.launch(headless=False)
    except Exception as e:
        print(f'{">"*20}Error: {e}{"<"*20}')


if __name__ == '__main__':
    main()