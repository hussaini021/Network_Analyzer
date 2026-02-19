import os
import NetworkAnalyzer
import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)

try:
    import NetworkAnalyzer
except Exception as e:
    print("FAILED TO LOAD VPN ENGINE")
    print(e)
    sys.exit(1)


def main():
    print("=== Network PRO ANALYSIS ===")

    if hasattr(NetworkAnalyzer, "check_dns"):
        print(NetworkAnalyzer.check_dns())

    if hasattr(NetworkAnalyzer, "check_webrtc"):
        print(NetworkAnalyzer.check_webrtc())

    if hasattr(NetworkAnalyzer, "check_proxy"):
        print(NetworkAnalyzer.check_proxy())

    if hasattr(NetworkAnalyzer, "risk_score"):
        print("RISK SCORE:", NetworkAnalyzer.risk_score())


if __name__ == "__main__":
    main()
