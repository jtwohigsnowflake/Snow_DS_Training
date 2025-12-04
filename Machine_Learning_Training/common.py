import ast


def get_next_model_version(df, model_name):
    """
    Check the model registry for a model name and return the next version number.
    If model doesn't exist, return 'V_1'.
    If model exists, increment the highest version number by 1.
    """
    # Check if dataframe is empty or model doesn't exist
    if df.empty or df[df["name"] == model_name].empty:
        return "V_1"

    # Get the model's versions
    model_row = df[df["name"] == model_name]
    versions_str = model_row["versions"].iloc[0]

    try:
        # Parse the versions list
        versions_list = ast.literal_eval(versions_str)

        # Extract version numbers and find the highest
        version_numbers = []
        for version in versions_list:
            # Handle different version formats (V_1, V_2, etc.)
            if "_" in version:
                try:
                    # Split on last underscore and get the number part
                    parts = version.rsplit("_", 1)
                    if len(parts) == 2 and parts[1].isdigit():
                        version_numbers.append(int(parts[1]))
                except:
                    continue

        if version_numbers:
            # Get the highest version number and increment
            max_version = max(version_numbers)
            return f"V_{max_version + 1}"
        else:
            # If no valid version numbers found, start with V_1
            return "V_1"

    except Exception as e:
        print(f"Error parsing versions: {e}")
        return "V_1"
