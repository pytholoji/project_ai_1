# project_ai_1

## Projeyi indir
  - **Projeyi git üzerinden indir.**
  ```term
  git clone https://github.com/pytholoji/project_ai_1.git
  ```

## Kodu çalıştırmadan Önce!
  - Proje en son sürüme gelmeli.
  1. **Proje klasörüne gir.**
  - `cd project_ai_1`
  2. **Projeyi güncelle.**
  - `git pull`
  3. **Python ortamı oluştur.**
  - Öncelikle python sürümünü 3.12.8 olarak değiştir.
  - Linux'ta pyenv kullanılabilir. `pyenv virtualenv 3.12.8 yapayzeka` bu aynı zamanda yeni venv açar.
  - Windows'ta [python.org](https://www.python.org/downloads/release/python-3128/) sitesinden Windows installer'ı indir.
  - ***NOT: Açacağınız sanal ortam project_ai_1 git klasörünün dışında olmasında fayda var.***_
  - Sonrasında: `python -m venv yapayzeka` yazarak yeni ortamını oluştur. (linux için de aynısı)
  4. **Python sanal ortamını aktive et.**
  - pyenv kullanarak: `pyenv activate yapayzeka` -> 'yapayzeka' yerine sizin venv'e verdiğiniz ismi giriniz.
  - Windows'ta : `yapayzeka\Scripts\activate` -> 'yapayzeka' yerine sizin venv'e verdiğiniz ismi giriniz.
  - Linux'ta: `. ./yapayzeka/Scripts/activate` -> 'yapayzeka' yerine sizin venv'e verdiğiniz ismi giriniz.
  5. **Gerekli kütüphaneleri indir.**
  - linux: `python3 -m pip install -r requirements.txt`
  - windows: `python -m pip install -r requirements.txt`
  6. **Artık çalıştırılmaya müsait!**
  - `python ./ornek.py` -> örnek python dosyasını çalıştırarak test edebilirsiniz!
