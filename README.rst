denite-fasd.nvim
================

A [denite.nvim](https://github.com/Shougo/denite.nvim) source for [fasd](https://github.com/clvv/fasd).

To install with `vim-plug`:

.. code:: vim

    Plug 'Shougo/denite.nvim'
    Plug 'raineszm/denite-fasd.nvim'

To install with `dein`:


.. code:: vim

    ...
    call dein#add('denite.nvim')
    call dein#add('raineszm/denite-fasd.nvim')

To use denite-fasd call

.. code:: vim

    :Denite fasd:argument

Calling without an argument (i.e. `:Denite fasd`) will prompt interatively for an argument.
