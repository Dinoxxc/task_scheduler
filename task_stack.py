# task_stack.py

class TaskStack:
    def __init__(self):
        self.stack = []  # List untuk menyimpan tugas (LIFO)

    def is_empty(self):
        return len(self.stack) == 0

    def push_task(self, task):
        """Menambahkan task (dictionary) ke bagian paling atas dari stack."""
        self.stack.append(task)

    def pop_task(self):
        """Menghapus dan mengembalikan task paling atas (terakhir ditambahkan)."""
        if not self.is_empty():
            return self.stack.pop()
        return None

    def update_task(self, index, new_task):
        """
        Update task berdasarkan index (0-based).
        new_task adalah dictionary yang akan menggantikan dictionary lama di index tersebut.
        """
        if 0 <= index < len(self.stack):
            self.stack[index] = new_task
            return True
        return False

    def delete_task(self, index):
        """
        Menghapus task berdasarkan index (0-based).
        Pastikan index valid, yaitu 0 <= index < len(self.stack).
        """
        if 0 <= index < len(self.stack):
            self.stack.pop(index)
            return True
        return False

    def search_task(self, keyword):
        """
        Mencari keyword pada field 'title', 'due_date', atau 'deskripsi'.
        Mengembalikan daftar tuple (index, task_dict).
        """
        results = []
        for i, task in enumerate(self.stack):
            title_str = task['title'].lower()
            due_str = task['due_date'].lower()
            desc_str = task['deskripsi'].lower()  # cari juga di deskripsi
            if (keyword.lower() in title_str) or (keyword.lower() in due_str) or (keyword.lower() in desc_str):
                results.append((i, task))
        return results

    def show_all_tasks(self, lang_dict):
        """
        Menampilkan seluruh tugas di dalam stack (dari 1 ke akhir).
        Menggunakan enumerate(start=1) agar penomoran di layar mulai dari 1.
        """
        if self.is_empty():
            print(lang_dict['no_tasks'])
        else:
            print(lang_dict['show_all'])
            for nomor, task in enumerate(self.stack, start=1):
                print(
                    f"{lang_dict['index']} {nomor}:\n"
                    f"  {lang_dict['title']}    : {task['title']}\n"
                    f"  {lang_dict['due_date']}: {task['due_date']}\n"
                    f"  {lang_dict['priority']}: {task['priority']}\n"
                    f"  {lang_dict['desc']}    : {task['deskripsi']}\n"
                )
