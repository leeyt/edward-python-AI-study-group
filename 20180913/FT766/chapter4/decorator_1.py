# 啟用decorator（debug_log）功能的旗標`
debug_trace = True
# 當上述旗標啟用時，開啟log檔案
if debug_trace:
    log_file = open("debug.log", "w", encoding='utf-8')


# decorator函式的定義
def debug_log(func):
    if debug_trace:
        def func_and_log(*args, **kwargs):
            # 執行func前記錄於log檔案
            log_file.write("開始 %s: %s, %s\n" %
                           (func.__name__, args, kwargs))
            # 直接執行func
            r = func(*args, **kwargs)
            # func結束時再次記錄於log檔案
            log_file.write("結束 %s: 回傳值 %s\n" % (func.__name__, r))
            return r
        return func_and_log
    else:
        return func  # 若debug_trace = False則什麼也沒變


# 以decorator變更myFunc的功能
@debug_log
def myfunc(x):
    return x+x

# 執行以decorator變更後的myFunc
myfunc(3)
myfunc(5)
log_file.close()  # 關閉log檔案
