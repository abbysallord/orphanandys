#!/usr/bin/env python3
"""
Backend API Testing for Orphan Andy's Restaurant
Tests all 4 main API endpoints with comprehensive validation
"""

import requests
import json
from typing import Dict, List, Any
import sys
from datetime import datetime

# Backend URL from frontend environment
BACKEND_URL = "https://classic-diner-sf.preview.emergentagent.com/api"

class APITester:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.results = {
            "total_tests": 0,
            "passed": 0,
            "failed": 0,
            "errors": []
        }
    
    def log_result(self, test_name: str, passed: bool, message: str = ""):
        """Log test result"""
        self.results["total_tests"] += 1
        if passed:
            self.results["passed"] += 1
            print(f"✅ {test_name}: PASSED {message}")
        else:
            self.results["failed"] += 1
            self.results["errors"].append(f"{test_name}: {message}")
            print(f"❌ {test_name}: FAILED - {message}")
    
    def test_endpoint(self, endpoint: str, expected_count: int = None, required_fields: List[str] = None) -> Dict[str, Any]:
        """Generic endpoint tester"""
        url = f"{self.base_url}{endpoint}"
        try:
            print(f"\n🔍 Testing {endpoint}")
            print(f"URL: {url}")
            
            response = requests.get(url, timeout=10)
            
            # Test status code
            if response.status_code == 200:
                self.log_result(f"{endpoint} - Status Code", True, f"(200)")
            else:
                self.log_result(f"{endpoint} - Status Code", False, f"Expected 200, got {response.status_code}")
                return {"success": False, "data": None}
            
            # Test JSON parsing
            try:
                data = response.json()
                self.log_result(f"{endpoint} - JSON Parse", True)
            except json.JSONDecodeError as e:
                self.log_result(f"{endpoint} - JSON Parse", False, f"Invalid JSON: {str(e)}")
                return {"success": False, "data": None}
            
            # Test expected count
            if expected_count is not None:
                if isinstance(data, list):
                    actual_count = len(data)
                    if actual_count == expected_count:
                        self.log_result(f"{endpoint} - Item Count", True, f"({actual_count} items)")
                    else:
                        self.log_result(f"{endpoint} - Item Count", False, f"Expected {expected_count}, got {actual_count}")
                else:
                    self.log_result(f"{endpoint} - Item Count", False, f"Expected list with {expected_count} items, got {type(data)}")
            
            # Test required fields
            if required_fields:
                if isinstance(data, list) and len(data) > 0:
                    first_item = data[0]
                    missing_fields = [field for field in required_fields if field not in first_item]
                    if not missing_fields:
                        self.log_result(f"{endpoint} - Required Fields", True, f"({', '.join(required_fields)})")
                    else:
                        self.log_result(f"{endpoint} - Required Fields", False, f"Missing fields: {missing_fields}")
                elif isinstance(data, dict):
                    missing_fields = [field for field in required_fields if field not in data]
                    if not missing_fields:
                        self.log_result(f"{endpoint} - Required Fields", True, f"({', '.join(required_fields)})")
                    else:
                        self.log_result(f"{endpoint} - Required Fields", False, f"Missing fields: {missing_fields}")
            
            return {"success": True, "data": data}
            
        except requests.exceptions.RequestException as e:
            self.log_result(f"{endpoint} - Connection", False, f"Request failed: {str(e)}")
            return {"success": False, "data": None}
        except Exception as e:
            self.log_result(f"{endpoint} - General", False, f"Unexpected error: {str(e)}")
            return {"success": False, "data": None}
    
    def test_menu_api(self):
        """Test GET /api/menu endpoint"""
        print("\n" + "="*50)
        print("TESTING MENU API")
        print("="*50)
        
        result = self.test_endpoint(
            "/menu",
            expected_count=9,
            required_fields=["_id", "name", "description", "price", "image", "category"]
        )
        
        if result["success"] and result["data"]:
            data = result["data"]
            # Additional validation for menu items
            if isinstance(data, list) and len(data) > 0:
                sample_item = data[0]
                
                # Check data types
                if isinstance(sample_item.get("price"), str):
                    self.log_result("Menu - Price Type", True, "(string)")
                else:
                    self.log_result("Menu - Price Type", False, f"Expected string, got {type(sample_item.get('price'))}")
                
                if isinstance(sample_item.get("name"), str):
                    self.log_result("Menu - Name Type", True, "(string)")
                else:
                    self.log_result("Menu - Name Type", False, f"Expected string, got {type(sample_item.get('name'))}")
                
                print(f"📋 Sample menu item: {sample_item.get('name')} - ${sample_item.get('price')}")
    
    def test_reviews_api(self):
        """Test GET /api/reviews/stats endpoint"""
        print("\n" + "="*50)
        print("TESTING REVIEWS API")
        print("="*50)
        
        result = self.test_endpoint(
            "/reviews/stats",
            required_fields=["average", "total", "breakdown", "popularKeywords"]
        )
        
        if result["success"] and result["data"]:
            data = result["data"]
            
            # Check average rating
            average = data.get("average")
            if average == 4.5:
                self.log_result("Reviews - Average Rating", True, f"({average})")
            else:
                self.log_result("Reviews - Average Rating", False, f"Expected 4.5, got {average}")
            
            # Check total reviews
            total = data.get("total")
            if total == 2387:
                self.log_result("Reviews - Total Count", True, f"({total})")
            else:
                self.log_result("Reviews - Total Count", False, f"Expected 2387, got {total}")
            
            # Check breakdown is array
            breakdown = data.get("breakdown")
            if isinstance(breakdown, list):
                self.log_result("Reviews - Breakdown Type", True, f"(array with {len(breakdown)} items)")
            else:
                self.log_result("Reviews - Breakdown Type", False, f"Expected array, got {type(breakdown)}")
            
            # Check popularKeywords is array
            keywords = data.get("popularKeywords")
            if isinstance(keywords, list):
                self.log_result("Reviews - Keywords Type", True, f"(array with {len(keywords)} items)")
            else:
                self.log_result("Reviews - Keywords Type", False, f"Expected array, got {type(keywords)}")
            
            print(f"⭐ Average: {average}, Total: {total} reviews")
    
    def test_busy_times_api(self):
        """Test GET /api/busy-times endpoint"""
        print("\n" + "="*50)
        print("TESTING BUSY TIMES API")
        print("="*50)
        
        result = self.test_endpoint(
            "/busy-times",
            expected_count=8,
            required_fields=["hour", "value"]
        )
        
        if result["success"] and result["data"]:
            data = result["data"]
            if isinstance(data, list) and len(data) > 0:
                sample_item = data[0]
                
                # Check hour is string
                if isinstance(sample_item.get("hour"), str):
                    self.log_result("BusyTimes - Hour Type", True, "(string)")
                else:
                    self.log_result("BusyTimes - Hour Type", False, f"Expected string, got {type(sample_item.get('hour'))}")
                
                # Check value is number (percentage)
                value = sample_item.get("value")
                if isinstance(value, (int, float)):
                    self.log_result("BusyTimes - Value Type", True, f"(number: {value})")
                else:
                    self.log_result("BusyTimes - Value Type", False, f"Expected number, got {type(value)}")
                
                print(f"📊 Sample time slot: {sample_item.get('hour')} - {sample_item.get('value')}%")
    
    def test_gallery_api(self):
        """Test GET /api/gallery endpoint"""
        print("\n" + "="*50)
        print("TESTING GALLERY API")
        print("="*50)
        
        result = self.test_endpoint(
            "/gallery",
            expected_count=8,
            required_fields=["url", "alt"]
        )
        
        if result["success"] and result["data"]:
            data = result["data"]
            if isinstance(data, list) and len(data) > 0:
                sample_item = data[0]
                
                # Check url is string
                if isinstance(sample_item.get("url"), str):
                    self.log_result("Gallery - URL Type", True, "(string)")
                else:
                    self.log_result("Gallery - URL Type", False, f"Expected string, got {type(sample_item.get('url'))}")
                
                # Check alt is string
                if isinstance(sample_item.get("alt"), str):
                    self.log_result("Gallery - Alt Type", True, "(string)")
                else:
                    self.log_result("Gallery - Alt Type", False, f"Expected string, got {type(sample_item.get('alt'))}")
                
                print(f"🖼️ Sample image: {sample_item.get('alt')}")
    
    def run_all_tests(self):
        """Run all API tests"""
        print("🚀 Starting Orphan Andy's Restaurant Backend API Tests")
        print(f"🌐 Backend URL: {self.base_url}")
        print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Test all endpoints
        self.test_menu_api()
        self.test_reviews_api()
        self.test_busy_times_api()
        self.test_gallery_api()
        
        # Print summary
        print("\n" + "="*60)
        print("TEST SUMMARY")
        print("="*60)
        print(f"Total Tests: {self.results['total_tests']}")
        print(f"✅ Passed: {self.results['passed']}")
        print(f"❌ Failed: {self.results['failed']}")
        
        if self.results['errors']:
            print("\n🚨 FAILED TESTS:")
            for error in self.results['errors']:
                print(f"  • {error}")
        
        success_rate = (self.results['passed'] / self.results['total_tests']) * 100 if self.results['total_tests'] > 0 else 0
        print(f"\n📊 Success Rate: {success_rate:.1f}%")
        
        if self.results['failed'] == 0:
            print("\n🎉 ALL TESTS PASSED! Backend APIs are working correctly.")
            return True
        else:
            print(f"\n⚠️ {self.results['failed']} tests failed. Please check the issues above.")
            return False

def main():
    """Main test execution"""
    tester = APITester(BACKEND_URL)
    success = tester.run_all_tests()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()