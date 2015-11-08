#coding: utf-8


def strfdelta(tdelta, fmt):
    """timedelta convert string
    ex: strfdelta(delta_obj, "{hours} hours and {minutes} to go")
    => 20 hours and 18 to go"""
    d = {"days": tdelta.days}
    d["hours"], rem = divmod(tdelta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return fmt.format(**d)