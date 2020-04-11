if !has('python3')
  echo "Error: Required vim compiled with +python3"
  finish
endif

python3 << endOfPython
import sys
import vim
sys.path.append(vim.eval('expand("<sfile>:h")'))
endOfPython

function! DetectIndent()
python3 << endOfPython
import indentdetective as idet
use = idet.decide(idet.statistics(vim.current.buffer))
if use == idet.USE_TABS:
    vim.command("setlocal noexpandtab")
elif use == idet.USE_SPACES:
    vim.command("setlocal expandtab")
endOfPython
endfunction

augroup indentdetective
  au!
  au BufReadPost * :call DetectIndent()
augroup END
