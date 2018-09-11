denite-fasd.nvim
================

A `denite.nvim`_ source for `fasd`_.

To install with `vim-plug`_:

.. code:: vim

    Plug 'Shougo/denite.nvim'
    Plug 'raineszm/denite-fasd.nvim'

To install with `dein`_:


.. code:: vim

    ...
    call dein#add('denite.nvim')
    call dein#add('raineszm/denite-fasd.nvim')

To use denite-fasd call

.. code:: vim

    :Denite fasd:argument

Calling without an argument (i.e. :code:`:Denite fasd`) will prompt interatively for an argument.

.. _denite: https://github.com/Shougo/denite.nvim
.. _fasd: https://github.com/clvv/fasd
.. _dein: https://github.com/Shougo/dein.vim
.. _vim-plug: https://github.com/junegunn/vim-plug
