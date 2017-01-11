# ZSH toolbox:

__TOOLBOX_DIR="${0:A:h}"

function UTF8-GBK() {
    local get_new_name="$__TOOLBOX_DIR/get_new_name.py"
    _NEW_NAME=$(python ${get_new_name} -i $1 -f convert_results 2>/dev/null)
    if [ -z "${_NEW_NAME}" ]; then
        echo "Please check that if your file exits."
    else
        iconv -f UTF8 -t GB18030 $1 > ${_NEW_NAME}
        echo "the new file is:${_NEW_NAME}"
    fi
}
