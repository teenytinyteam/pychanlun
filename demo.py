from pychanlun.chan import Chan

if __name__ == '__main__':
    chan = Chan('AAPL')
    print(chan.get_sticks('1m'))
    print(chan.get_fractals('1m'))
    print(chan.get_strokes('1m'))
    print(chan.get_stroke_pivots('1m'))
    print(chan.get_stroke_pivot_trends('1m'))
    print(chan.get_stroke_pivot_signals('1m'))
    print(chan.get_segments('1m'))
    print(chan.get_segment_pivots('1m'))
    print(chan.get_segment_pivot_trends('1m'))
    print(chan.get_segment_pivot_signals('1m'))