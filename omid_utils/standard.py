import re


def persian_num_to_english(string):
    return string.strip().replace('۰', '0').replace('۱', '1').replace('۲', '2').replace('۳', '3') \
        .replace('۴', '4').replace('۵', '5').replace('۶', '6').replace('۷', '7'). \
        replace('۸', '8').replace('۹', '9')


def standard_persian(string):
    return string.strip().replace('ي', 'ی').replace('ؠ', 'ی').replace('ى', 'ی').replace('ك', 'ک') \
        .replace('ٶ', 'و').replace('ؤ', 'و').replace('‌', ' ')


def clear_swift(string):
    ans = string.encode("ascii", errors="ignore").decode().strip().replace('\r', '\n')
    ans = re.sub('\n+', '\n', ans)
    ans = re.sub(' +', ' ', ans)
    ans = re.sub('}\s*{', '}{', ans)
    ans = ans.replace('!', '')
    return ans


def swift_number_to_float(string):
    string = str(string)
    spl = string.split(',')
    if len(spl) == 2:
        if len(spl[1]) == 1 or len(spl[1]) == 2:
            return float(string.replace(',', '.'))
    return float(string.replace(',',''))
