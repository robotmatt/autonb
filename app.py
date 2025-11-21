import streamlit as st
import time
from datetime import datetime
from seleniumSetup import seleniumSetup
from browserSetup import browserSetup
from basicRun import basicRun
from unstackRun import unstackRun
import config
from run_logic import generate_run_params

# Page config
st.set_page_config(page_title="AutoNB", page_icon="🛫", layout="wide")

st.title("🛫 AutoNB: Automated Navblue PBS Runs")

# Configuration Section
with st.expander("Configuration", expanded=True):
    # Run Settings
    st.subheader("Run Settings")
    c1, c2, c3, c4, c5, c6 = st.columns(6)
    with c1:
        run_count_options = [f"{i:04d}" for i in range(0, 31000, 1000)]
        try:
            default_index = run_count_options.index(f"{config.runcount:04d}")
        except ValueError:
            default_index = 0
        runcount = int(st.selectbox("Run Count", run_count_options, index=default_index))
    with c2:
        selected_base = st.selectbox("Base", ["IAH", "IAD"], index=0 if "IAH" in config.baseList else 1)
        baseList = [selected_base]
    with c3:
        seat = st.selectbox("Seat", ["CA", "FO"], index=0 if config.seat == "CA" else 1)
    with c4:
        prefix = st.text_input("Prefix", value=config.prefix)
    with c5:
        suffix = st.text_input("Suffix", value=config.suffix)
    with c6:
        max_iter_options = [2000002, 3000003, 5000005, 7000007, 10000001]
        try:
            default_iter_index = max_iter_options.index(config.maxIterations)
        except ValueError:
            default_iter_index = 0
        maxIterations = st.selectbox("Max Iterations", max_iter_options, index=default_iter_index)


    # Credit Windows
    st.subheader("Credit Windows")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Minimum Window**")
        w1, w2, w3 = st.columns(3)
        with w1:
            minFloor = st.number_input("Minimum Floor", value=config.minFloor)
        with w2:
            minCeiling = st.number_input("Minimum Ceiling", value=config.minCeiling)
        with w3:
            minThresholdIncrement = st.selectbox("Minimum Increment", [15, 30, 60], index=[15, 30, 60].index(config.minThresholdIncrement))
    with c2:
        st.markdown("**Normal Window**")
        w1, w2, w3 = st.columns(3)
        with w1:
            normalFloor = st.number_input("Normal Floor", value=config.normalFloor)
        with w2:
            normalCeiling = st.number_input("Normal Ceiling", value=config.normalCeiling)
        with w3:
            normThresholdIncrement = st.selectbox("Normal Increment", [15, 30, 60], index=[15, 30, 60].index(config.normThresholdIncrement))
    with c3:
        st.markdown("**Maximum Window**")
        w1, w2, w3 = st.columns(3)
        with w1:
            maxFloor = st.number_input("Maximum Floor", value=config.maxFloor)
        with w2:
            maxCeiling = st.number_input("Maximum Ceiling", value=config.maxCeiling)
        with w3:
            maxThresholdIncrement = st.selectbox("Maximum Increment", [15, 30, 60], index=[15, 30, 60].index(config.maxThresholdIncrement))
    
    st.subheader("Other Window Settings")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown("**Mixed Line Settings**")
        x1, x2, x3 = st.columns(3)
        with x1:
            mixed_low = st.number_input("Mixed Low", value=config.mixed_low)
        with x2:
            mixed_high = st.number_input("Mixed High", value=config.mixed_high)
        with x3:
            mixed_threshold = st.number_input("Mixed Threshold", value=config.mixed_threshold)
    with m2:
        st.markdown("**Split Credit**")
        s1, s2, s3 = st.columns(3)
        with s1:
            split_low = st.number_input("Split Low", value=config.split_low)
        with s2:
            split_high = st.number_input("Split High", value=config.split_high)
        with s3:
            split_threshold = st.number_input("Split Threshold", value=config.split_threshold)
    with m3:
        st.markdown("**Max Mixed Lines**")
        maxMixedLines = st.number_input("Max Mixed Lines", value=config.maxMixedLines)

    # System & Limits
    st.subheader("System & Limits")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("**System**")
        productionServer = st.checkbox("Production Server", value=config.productionServer)
        testMode = st.checkbox("Test Mode (Dry Run)", value=config.testMode)
        verbose = st.checkbox("Verbose Logging", value=config.verbose)
        
        # Check for credentials
        try:
            import userInfo
            file_username = getattr(userInfo, 'username', '')
            file_password = getattr(userInfo, 'password', '')
        except ImportError:
            file_username = ''
            file_password = ''
            
        if not file_username or not file_password:
            st.warning("Credentials missing in userInfo.py")
            input_username = st.text_input("Username")
            input_password = st.text_input("Password", type="password")
        else:
            input_username = file_username
            input_password = file_password
    with c2:
        st.markdown("**Limits**")
        maxMinCredit = st.number_input("Max Min Credit (0 for no restriction)", value=config.maxMinCredit)

    # Advanced Configuration
    with st.expander("⚙️ Advanced Configuration", expanded=False):
        st.markdown("**Server URLs**")
        url_col1, url_col2 = st.columns(2)
        with url_col1:
            production_url = st.text_input(
                "Production Server URL",
                value="https://uca.pbs.vmc.navblue.cloud/cgi-bin-xml/class/main.cgi",
                help="URL for the production PBS server"
            )
        with url_col2:
            uat_url = st.text_input(
                "UAT Server URL",
                value="https://uca-uat.pbs.vmc.navblue.cloud/cgi-bin-xml/class/login.cgi",
                help="URL for the UAT/testing PBS server"
            )

# Help Section (Sidebar)
with st.sidebar:
    st.markdown("## ℹ️ Help & Documentation")
    st.markdown("### Coming Soon")
    st.info("Detailed documentation and help content will be added here.")
    # TODO: Add comprehensive help documentation


# Main Execution Area
st.header("Execution")

tab_basic, tab_unstack = st.tabs(["Basic Run", "Unstack Run"])

with tab_basic:
    st.subheader("Basic Run Configuration")
    # Basic run doesn't have many specific settings exposed yet that aren't global
    
    if st.button("Start Basic Run", type="primary"):
        st.write("Starting Basic Run...")
        
        # Setup Browser
        try:
            browser = seleniumSetup()
            browserSetup(browser, productionServer, input_username, input_password, production_url, uat_url)
            time.sleep(5)  # wait for javascript

            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d_%H:%M:%S")

            current_runcount = runcount
            status_text = st.empty()
            
            for run_data in generate_run_params(baseList, minFloor, minCeiling, minThresholdIncrement,
                                                maxFloor, maxCeiling, maxThresholdIncrement,
                                                normalFloor, normalCeiling, normThresholdIncrement):
                
                if run_data["valid"]:
                    base = run_data["base"]
                    status_text.text(f"Executing Run {current_runcount} for {base}...")
                    if verbose:
                        st.text(f"Run {current_runcount}: {base} {seat}")

                    basicRun(prefix, suffix, maxMinCredit, maxIterations, base, seat,
                             minFloor, minCeiling, run_data["minThresholdHour"], run_data["minThresholdMinute"],
                             normalFloor, normalCeiling, run_data["normalThresholdHour"],
                             run_data["normalThresholdMinute"], maxFloor, maxCeiling,
                             run_data["maxThresholdHour"], run_data["maxThresholdMinute"], split_low,
                             split_high, split_threshold, maxMixedLines, mixed_low, mixed_high, mixed_threshold,
                             browser, testMode, verbose,
                             current_runcount)
                    current_runcount += 1
                else:
                    if verbose: st.text(f"Skipping run {current_runcount}: {run_data['reason']}")
            
            st.success("Basic Runs Complete!")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")

with tab_unstack:
    st.subheader("Unstack Run Configuration")
    
    col_u1, col_u2 = st.columns(2)
    with col_u1:
        unstackLineHolders = st.number_input("Unstack Line Holders (0 to disable)", value=config.unstackLineHolders)
        maxPasses = st.number_input("Max Passes", value=config.maxPasses)
    with col_u2:
        pointOrDayStack = st.selectbox("Stack Type", ["day", "point"], index=0 if config.pointOrDayStack == "day" else 1)

    with st.expander("Day Settings (Unstack)", expanded=False):
        st.write("Set values for each day of the month:")
        day_settings = {}
        cols = st.columns(7)
        for day in range(1, 32):
            with cols[(day - 1) % 7]:
                # Default values based on the original hardcoded logic
                default_val = 20
                day_settings[day] = st.number_input(f"Day {day}", value=default_val, key=f"day_{day}")

    if st.button("Start Unstack Run", type="primary"):
        st.write("Starting Unstack Run...")
        
        # Setup Browser
        try:
            browser = seleniumSetup()
            browserSetup(browser, productionServer, input_username, input_password, production_url, uat_url)
            time.sleep(5)  # wait for javascript

            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d_%H:%M:%S")

            current_runcount = runcount
            status_text = st.empty()
            
            for run_data in generate_run_params(baseList, minFloor, minCeiling, minThresholdIncrement,
                                                maxFloor, maxCeiling, maxThresholdIncrement,
                                                normalFloor, normalCeiling, normThresholdIncrement):
                if run_data["valid"]:
                    base = run_data["base"]
                    status_text.text(f"Executing Run {current_runcount} for {base}...")
                    if verbose:
                        st.text(f"Run {current_runcount}: {base} {seat}")

                    unstackRun(prefix, suffix, maxMinCredit, maxIterations, base, seat,
                               minFloor, minCeiling, run_data["minThresholdHour"], run_data["minThresholdMinute"],
                               normalFloor, normalCeiling, run_data["normalThresholdHour"],
                               run_data["normalThresholdMinute"], maxFloor, maxCeiling,
                               run_data["maxThresholdHour"], run_data["maxThresholdMinute"], split_low,
                               split_high, split_threshold, maxMixedLines, unstackLineHolders, maxPasses,
                               pointOrDayStack, mixed_low, mixed_high, mixed_threshold, day_settings,
                               browser, testMode, verbose, current_runcount)
                                   
                    current_runcount += 1
                else:
                    if verbose: st.text(f"Skipping run {current_runcount}: {run_data['reason']}")
            
            st.success("Unstack Runs Complete!")
                
        except Exception as e:
            st.error(f"An error occurred: {e}")
