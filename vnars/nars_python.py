'''NARS-Python 源码的无 GUI 标准输入适配。
- 🎯复用现有 main 和输入解析入口，不更改推理规则。
- 📌该版本自主推进，不承诺显式周期或重放不变性。
- 🤖Agent 生成，尚未经人工接管审阅。
'''
from __future__ import annotations

import sys  # 标准输入与明确传入的源目录
from pathlib import Path  # 与调用者工作目录解耦


def run(root: Path) -> None:
    '''修正原输入线程放入 str、而处理器要求 tuple 的形状差异。'''
    sys.path.insert(0, str(root.resolve()))
    import Config
    import InputChannel

    Config.GUI_USE_INTERFACE = False  # 服务模式不打开桌面 GUI
    Config.SILENT_MODE = False
    Config.DEBUG = False

    class __FifoInput(list):
        '''原处理器使用 pop()；在适配边界使接收队列保持输入次序。'''
        def pop(self, index: int = 0):
            return super().pop(index)

    InputChannel.pended_input_data_queue = __FifoInput()

    def __read_input() -> None:
        '''使用 CIN 自己的排队 API，不改写任何推理步骤。'''
        for line in sys.stdin:
            InputChannel.parse_and_queue_input_string(line.rstrip('\r\n'))

    InputChannel.get_user_input = __read_input
    import main
    main.main()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('NARS-Python source directory is required')
    run(Path(sys.argv[1]))
