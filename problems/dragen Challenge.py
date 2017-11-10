def provide_path(list):
    path = []
    last = 0
    cur = 0
    last_r = 0
    m_pos = 0
    m_pos_range = 0
    while last_r < len(list)-1:
        for i in range(m_pos, last_r+1):
            tmp_pos = min(list[i]+i, len(list)-1)
            while list[tmp_pos] == 0:
                tmp_pos-=1
            if m_pos_range < tmp_pos:
                m_pos = i
                m_pos_range = tmp_pos
        path.append(i)
        if last_r == m_pos_range:
            return False
        last_r = m_pos_range
    path.append(len(list)-1)
    return path

print provide_path([1,5,2,3,0,1,1,1,5])
