from math import ceil

def calculate_progress_checks(match_time, time_step, progress_check_threshold):
    progress_check_steps = ceil(15 / (time_step / 1000.0))  
    total_checks = match_time / time_step  
    checks_per_progress_check = ceil(total_checks / progress_check_steps)  
    progress_checks = ceil(total_checks / checks_per_progress_check)  
    return progress_checks