import eel
from api.common_response import success_response, exception_response, error_response
from repository.yuzu import get_all_yuzu_release_infos
from config import config
import logging

logger = logging.getLogger(__name__)


@eel.expose
def open_yuzu_keys_folder():
    from module.yuzu import open_yuzu_keys_folder
    open_yuzu_keys_folder()
    return success_response()


@eel.expose
def get_yuzu_config():
    return config.yuzu.to_dict()


@eel.expose
def ask_and_update_yuzu_path():
    from module.dialogs import ask_folder
    folder = ask_folder()
    logger.info(f'select folder: {folder}')
    if folder:
        from config import update_yuzu_path
        update_yuzu_path(folder)
        return success_response(msg=f'修改 yuzu 目录至 {folder}')
    else:
        return error_response(100, '修改已取消')


@eel.expose
def get_yuzu_release_infos():
    try:
        return success_response(get_all_yuzu_release_infos())
    except Exception as e:
        return exception_response(e)


@eel.expose
def detect_yuzu_version():
    try:
        from module.yuzu import detect_yuzu_version
        return success_response(detect_yuzu_version())
    except Exception as e:
        return exception_response(e)


@eel.expose
def start_yuzu():
    from module.yuzu import start_yuzu
    try:
        start_yuzu()
        return success_response()
    except Exception as e:
        return exception_response(e)


@eel.expose
def install_yuzu(version):
    if not version or version == '':
        return {'msg': f'无效的版本 {version}'}
    from module.yuzu import install_yuzu
    return {'msg': install_yuzu(version)}


@eel.expose
def install_yuzu_firmware(version):
    if not version or version == '':
        return {'msg': f'无效的版本 {version}'}
    from module.yuzu import install_firmware_to_yuzu
    return {'msg': install_firmware_to_yuzu(version)}
