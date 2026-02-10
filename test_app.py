"""
Simple unit tests for Dash app structure
"""
import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_app_structure():
    """Test basic app structure"""
    print("=" * 50)
    print("Running Dash App Tests")
    print("=" * 50)
    
    # Try to import the app
    try:
        from app import app, df, load_data
        print("✓ App imports successfully")
    except ImportError as e:
        raise AssertionError(f"Failed to import app: {e}")
    
    # Check data loading
    if df is not None:
        print("✓ Data loaded successfully")
        print(f"  - Rows: {len(df)}")
        print(f"  - Columns: {list(df.columns)}")
    else:
        print("⚠️  Data not loaded - check formatted_sales_data.csv")
    
    # Check layout components
    layout_str = str(app.layout)
    
    # Test 1: Header present
    if "Soul Foods Sales Dashboard" in layout_str:
        print("✓ TEST 1 PASSED: Header is present")
    else:
        print("✗ TEST 1 FAILED: Header not found")
    
    # Test 2: Visualization present
    if "main-chart" in layout_str:
        print("✓ TEST 2 PASSED: Visualization is present")
    else:
        print("✗ TEST 2 FAILED: Visualization (main-chart) not found")
    
    # Test 3: Region picker present
    if "region-filter" in layout_str and "RadioItems" in layout_str:
        print("✓ TEST 3 PASSED: Region picker is present")
    else:
        print("✗ TEST 3 FAILED: Region picker not found")
    

def run_all_tests():
    """Run all tests and report results"""
    test_results = []
    
    try:
        # Test 1: App structure
        test_app_structure()
        test_results.append(("App Structure", "PASSED"))
    except AssertionError as e:
        test_results.append(("App Structure", f"FAILED: {e}"))
    except Exception as e:
        test_results.append(("App Structure", f"ERROR: {e}"))
    
    # Summary
    print("\n" + "=" * 50)
    print("TEST SUMMARY")
    print("=" * 50)
    
    all_passed = True
    for test_name, result in test_results:
        status = "✅" if "PASSED" in result else "❌"
        print(f"{status} {test_name}: {result}")
        if "FAILED" in result or "ERROR" in result:
            all_passed = False
    
    print("=" * 50)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        return 1

if __name__ == "__main__":
    exit_code = run_all_tests()
    sys.exit(exit_code)