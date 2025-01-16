# main.py
import colorama
from colorama import Fore, Style

# Mengimpor modul lain
from ascii_art import print_ascii_art
from languages import LANG_DICT
from quotes import get_random_quote
from task_stack import TaskStack

colorama.init(autoreset=True)

def main():
    # Pilihan bahasa di awal program
    print("Select Language / Pilih Bahasa:")
    print("1. English")
    print("2. Bahasa Indonesia")
    lang_choice = input("Your choice / Pilihan Anda: ").strip()

    if lang_choice == '1':
        current_lang = 'en'
    else:
        current_lang = 'id'

    # Tampilkan ASCII Art
    print_ascii_art()

    # Tampilkan teks welcome
    print(Fore.MAGENTA + Style.BRIGHT + LANG_DICT[current_lang]['welcome'] + Style.RESET_ALL)

    # Buat instance dari TaskStack
    task_manager = TaskStack()

    while True:
        print(Fore.MAGENTA + Style.BRIGHT + LANG_DICT[current_lang]['menu_title'] + Style.RESET_ALL)
        print(LANG_DICT[current_lang]['menu_insert'])
        print(LANG_DICT[current_lang]['menu_update'])
        print(LANG_DICT[current_lang]['menu_delete'])
        print(LANG_DICT[current_lang]['menu_search'])
        print(LANG_DICT[current_lang]['menu_show'])
        print(LANG_DICT[current_lang]['menu_pop'])
        print(LANG_DICT[current_lang]['menu_exit'])

        choice = input(Fore.CYAN + LANG_DICT[current_lang]['input_choice'] + Style.RESET_ALL)

        # ========== 1. Insert Task ==========
        if choice == '1':
            print(Fore.GREEN + LANG_DICT[current_lang]['insert_task_title'] + Style.RESET_ALL)
            title = input(LANG_DICT[current_lang]['task_title'])
            due_date = input(LANG_DICT[current_lang]['task_due'])
            priority = input(LANG_DICT[current_lang]['task_priority'])
            deskripsi = input(LANG_DICT[current_lang]['task_desc'])  # Minta deskripsi

            new_task = {
                "title": title,
                "due_date": due_date,
                "priority": priority,
                "deskripsi": deskripsi
            }
            task_manager.push_task(new_task)
            print(Fore.GREEN + LANG_DICT[current_lang]['task_added'].format(title) + Style.RESET_ALL)
            print(Fore.BLUE + LANG_DICT[current_lang]['motivation'] + get_random_quote(current_lang) + Style.RESET_ALL)

        # ========== 2. Update Task ==========
        elif choice == '2':
            if task_manager.is_empty():
                print(Fore.RED + LANG_DICT[current_lang]['empty_cannot_update'] + Style.RESET_ALL)
                continue

            print(Fore.GREEN + LANG_DICT[current_lang]['update_title'] + Style.RESET_ALL)
            task_manager.show_all_tasks(LANG_DICT[current_lang])

            try:
                idx_input = int(input(LANG_DICT[current_lang]['input_index_update']))
                # Karena di tampilan kita mulai dari 1, kita kurangi 1 untuk akses list
                idx = idx_input - 1

                print(Fore.CYAN + "--------------------------------" + Style.RESET_ALL)
                title = input(LANG_DICT[current_lang]['task_title'])
                due_date = input(LANG_DICT[current_lang]['task_due'])
                priority = input(LANG_DICT[current_lang]['task_priority'])
                deskripsi = input(LANG_DICT[current_lang]['task_desc'])

                updated_task = {
                    "title": title,
                    "due_date": due_date,
                    "priority": priority,
                    "deskripsi": deskripsi
                }
                success = task_manager.update_task(idx, updated_task)
                if success:
                    print(Fore.GREEN + LANG_DICT[current_lang]['task_updated'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + LANG_DICT[current_lang]['index_invalid'] + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + LANG_DICT[current_lang]['input_index_invalid'] + Style.RESET_ALL)

        # ========== 3. Delete Task ==========
        elif choice == '3':
            if task_manager.is_empty():
                print(Fore.RED + LANG_DICT[current_lang]['empty_cannot_update'] + Style.RESET_ALL)
                continue

            print(Fore.GREEN + LANG_DICT[current_lang]['delete_title'] + Style.RESET_ALL)
            task_manager.show_all_tasks(LANG_DICT[current_lang])

            try:
                idx_input = int(input(LANG_DICT[current_lang]['input_index_delete']))
                idx = idx_input - 1
                success = task_manager.delete_task(idx)
                if success:
                    print(Fore.GREEN + LANG_DICT[current_lang]['task_deleted'] + Style.RESET_ALL)
                else:
                    print(Fore.RED + LANG_DICT[current_lang]['index_invalid'] + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + LANG_DICT[current_lang]['input_index_invalid'] + Style.RESET_ALL)

        # ========== 4. Search Task ==========
        elif choice == '4':
            print(Fore.GREEN + LANG_DICT[current_lang]['search_title'] + Style.RESET_ALL)
            keyword = input(LANG_DICT[current_lang]['input_search'])
            results = task_manager.search_task(keyword)

            if results:
                print(Fore.YELLOW + LANG_DICT[current_lang]['search_result'] + Style.RESET_ALL)
                # results = list of (i, task), i = 0-based
                for i, task in results:
                    nomor = i + 1  # Tampilkan di layar mulai dari 1
                    print(
                        f"{LANG_DICT[current_lang]['index']} {nomor}:\n"
                        f"  {LANG_DICT[current_lang]['title']}    : {task['title']}\n"
                        f"  {LANG_DICT[current_lang]['due_date']}: {task['due_date']}\n"
                        f"  {LANG_DICT[current_lang]['priority']}: {task['priority']}\n"
                        f"  {LANG_DICT[current_lang]['desc']}    : {task['deskripsi']}\n"
                    )
            else:
                print(Fore.RED + LANG_DICT[current_lang]['search_none'] + Style.RESET_ALL)

        # ========== 5. Show All Tasks ==========
        elif choice == '5':
            task_manager.show_all_tasks(LANG_DICT[current_lang])

        # ========== 6. Pop Last Task (LIFO) ==========
        elif choice == '6':
            popped_task = task_manager.pop_task()
            if popped_task:
                print(Fore.GREEN + LANG_DICT[current_lang]['pop_success'].format(popped_task['title']) + Style.RESET_ALL)
            else:
                print(Fore.RED + LANG_DICT[current_lang]['pop_empty'] + Style.RESET_ALL)

        # ========== 0. Exit Program ==========
        elif choice == '0':
            print(Fore.CYAN + LANG_DICT[current_lang]['exit_program'] + Style.RESET_ALL)
            break

        # ========== Invalid Menu ==========
        else:
            print(Fore.RED + LANG_DICT[current_lang]['menu_invalid'] + Style.RESET_ALL)


if __name__ == "__main__":
    main()
