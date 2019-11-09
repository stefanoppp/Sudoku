FROM python:3

RUN git clone https://github.com/stefanoppp/Sudoku
WORKDIR /Sudoku


RUN pip install parametrized

CMD ["python", "test_sudoku.py"]
