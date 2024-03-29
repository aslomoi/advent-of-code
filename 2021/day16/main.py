from math import prod

input_txt = "005532447836402684AC7AB3801A800021F0961146B1007A1147C89440294D005C12D2A7BC992D3F4E50C72CDF29EECFD0ACD5CC016962099194002CE31C5D3005F401296CAF4B656A46B2DE5588015C913D8653A3A001B9C3C93D7AC672F4FF78C136532E6E0007FCDFA975A3004B002E69EC4FD2D32CDF3FFDDAF01C91FCA7B41700263818025A00B48DEF3DFB89D26C3281A200F4C5AF57582527BC1890042DE00B4B324DBA4FAFCE473EF7CC0802B59DA28580212B3BD99A78C8004EC300761DC128EE40086C4F8E50F0C01882D0FE29900A01C01C2C96F38FCBB3E18C96F38FCBB3E1BCC57E2AA0154EDEC45096712A64A2520C6401A9E80213D98562653D98562612A06C0143CB03C529B5D9FD87CBA64F88CA439EC5BB299718023800D3CE7A935F9EA884F5EFAE9E10079125AF39E80212330F93EC7DAD7A9D5C4002A24A806A0062019B6600730173640575A0147C60070011FCA005000F7080385800CBEE006800A30C023520077A401840004BAC00D7A001FB31AAD10CC016923DA00686769E019DA780D0022394854167C2A56FB75200D33801F696D5B922F98B68B64E02460054CAE900949401BB80021D0562344E00042A16C6B8253000600B78020200E44386B068401E8391661C4E14B804D3B6B27CFE98E73BCF55B65762C402768803F09620419100661EC2A8CE0008741A83917CC024970D9E718DD341640259D80200008444D8F713C401D88310E2EC9F20F3330E059009118019A8803F12A0FC6E1006E3744183D27312200D4AC01693F5A131C93F5A131C970D6008867379CD3221289B13D402492EE377917CACEDB3695AD61C939C7C10082597E3740E857396499EA31980293F4FD206B40123CEE27CFB64D5E57B9ACC7F993D9495444001C998E66B50896B0B90050D34DF3295289128E73070E00A4E7A389224323005E801049351952694C000"
integer = int(input_txt, 16)
input_bin = format(integer, 'b').zfill(len(input_txt)*4)

sum_v = 0
operate = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}


def packet(bits):
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    global sum_v
    sum_v += version

    if type_id == 4:
        i = 6
        num = ''
        while True:
            if bits[i] == '1':
                num += bits[i+1:i+5]
                i += 5
            elif bits[i] == '0':
                num += bits[i+1:i+5]
                i += 5
                rem = bits[i:]
                break
        literal = int(num, 2)
        return (rem, literal)
    else:
        length_id = bits[6]
        vals = []

        if length_id == '0':
            length = int(bits[7:22], 2)
            rem = bits[22:22+length]
            while int(rem or '0', 2) != 0:
                rem, literal = packet(rem)
                vals.append(literal)
            rem = bits[22+length:]
        elif length_id == '1':
            num_sub = int(bits[7:18], 2)
            rem = bits[18:]
            for _ in range(num_sub):
                rem, literal = packet(rem)
                vals.append(literal)
        val = operate[type_id](vals)
        return (rem, val)


_, val = packet(input_bin)
print(f'Value: {val}')
print(f'Sum Version: {sum_v}')
