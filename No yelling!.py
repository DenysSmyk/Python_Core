def filter_words(st):
    st_sp = st.split()
    st_jo = ' '.join(st_sp)
    return st_jo[0].upper()+st_jo[1:].lower()