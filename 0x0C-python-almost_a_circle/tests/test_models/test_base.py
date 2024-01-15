#!/usr/bin/python3
"""Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(15, Base(15).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(15)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(15)
        b.id = 20
        self.assertEqual(20, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(15).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(6.6, Base(6.6).id)

    def test_complex_id(self):
        self.assertEqual(complex(8), Base(complex(8)).id)

    def test_dict_id(self):
        self.assertEqual({"x": 1, "y": 2}, Base({"x": 1, "y": 2}).id)

    def test_bool_id(self):
        self.assertEqual(False, Base(False).id)

    def test_list_id(self):
        self.assertEqual([4, 5, 6], Base([4, 5, 6]).id)

    def test_tuple_id(self):
        self.assertEqual((3, 7), Base((3, 7)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({7, 8, 9}), Base(frozenset({7, 8, 9})).id)

    def test_range_id(self):
        self.assertEqual(range(6), Base(range(6)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Programming', Base(b'Programming').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'abcdefg'), Base(bytearray(b'abcdefg')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'abcdefg'), Base(memoryview(b'abcdefg')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(11, 8, 3, 10, 7)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(11, 8, 3, 10, 7)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 61)

    def test_to_json_string_rectangle_two_dicts(self):
        r1 = Rectangle(4, 6, 8, 15, 4)
        r2 = Rectangle(9, 3, 7, 2, 13)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 122)

    def test_to_json_string_square_type(self):
        s = Square(12, 3, 4, 6)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_square_one_dict(self):
        s = Square(12, 3, 4, 6)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 53)

    def test_to_json_string_square_two_dicts(self):
        s1 = Square(7, 5, 2, 4)
        s2 = Square(2, 9, 8, 3)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_to_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(8, 6, 1, 3, 10)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 69)

    def test_save_to_file_two_rectangles(self):
        r1 = Rectangle(8, 6, 1, 3, 10)
        r2 = Rectangle(4, 2, 7, 1, 8)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 137)

    def test_save_to_file_one_square(self):
        s = Square(6, 4, 2, 9)
        Square.save_to_file        ([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_two_squares(self):
        s1 = Square(6, 4, 2, 9)
        s2 = Square(3, 7, 1, 5)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 106)

    def test_save_to_file_cls_name_for_filename(self):
        s = Square(6, 4, 2, 9)
        Base.save_to_file([s])
        with open("Base.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_overwrite(self):
        s = Square(7, 2, 1, 4)
        Square.save_to_file([s])
        s = Square(6, 4, 2, 9)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 1)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    def test_from_json_string_type(self):
        list_input = [{"id": 20, "width": 5, "height": 3}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 20, "width": 5, "height": 3, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
            {"id": 20, "width": 5, "height": 3, "x": 7, "y": 8},
            {"id": 21, "width": 8, "height": 2, "x": 3, "y": 5},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_one_square(self):
        list_input = [{"id": 20, "size": 5, "height": 3}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_squares(self):
        list_input = [
            {"id": 20, "size": 5, "height": 3},
            {"id": 21, "size": 2, "height": 8}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    def test_create_rectangle_original(self):
        r1 = Rectangle(4, 7, 1, 2, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (6) 1/2 - 4/7", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(4, 7, 1, 2, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (6) 1/2 - 4/7", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(4, 7, 1, 2, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(4, 7, 1, 2, 6)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        s1 = Square(5, 3, 1, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (8) 3/1 - 5", str(s1))

    def test_create_square_new(self):
        s1 = Square(5, 3, 1, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual("[Square] (8) 3/1 - 5", str(s2))

    def test_create_square_is(self):
        s1 = Square(5, 3, 1, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        s1 = Square(5, 3, 1, 8)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(5, 2, 8, 7,10)
        Rectangle.save_to_file([r1])
        r2 = Rectangle.load_from_file()[0]
        self.assertEqual("[Rectangle] (10) 7/10 - 5/2", str(r2))

    def test_load_from_file_first_square(self):
        s1 = Square(3, 4, 2, 6)
        Square.save_to_file([s1])
        s2 = Square.load_from_file()[0]
        self.assertEqual("[Square] (6) 4/2 - 3", str(s2))

    def test_load_from_file_two_rectangles(self):
        r1 = Rectangle(5, 2, 8, 7, 10)
        r2 = Rectangle(3, 7, 1, 1, 11)
        Rectangle.save_to_file([r1, r2])
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual("[Rectangle] (10) 7/10 - 5/2", str(list_rectangles[0]))
        self.assertEqual("[Rectangle] (11) 1/1 - 3/7", str(list_rectangles[1]))

    def test_load_from_file_two_squares(self):
        s1 = Square(3, 4, 2, 6)
        s2 = Square(8, 2, 1, 7)
        Square.save_to_file([s1, s2])
        list_squares = Square.load_from_file()
        self.assertEqual("[Square] (6) 4/2 - 3", str(list_squares[0]))
        self.assertEqual("[Square] (7) 2/1 - 8", str(list_squares[1]))

    def test_load_from_file_empty_file(self):
        with open("Rectangle.json", "w") as f:
            f.write("")
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual([], list_rectangles)

    def test_load_from_file_no_file(self):
        list_rectangles = Rectangle.load_from_file()
        self.assertEqual([], list_rectangles)

    def test_load_from_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file()

    def test_load_from_file_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.load_from_file([])


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(8, 6, 1, 3, 10)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_csv_two_rectangles(self):
        r1 = Rectangle(8, 6, 1, 3, 10)
        r2 = Rectangle(4, 2, 7, 1, 8)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue(len(f.read()) == 107)

    def test_save_to_file_csv_one_square(self):
        s = Square(6, 4, 2, 9)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue(len(f.read()) == 41)

    def test_save_to_file_csv_two_squares(self):
        s1 = Square(6, 4, 2, 9)
        s2 = Square(3, 7, 1, 5)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue(len(f.read()) == 83)

    def test_save_to_file_csv_cls_name_for_filename(self):
        s = Square(6, 4, 2, 9)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue(len(f.read()) == 41)

    def test_save_to_file_csv_overwrite(self):
        s = Square(7, 2, 1, 4)
        Square.save_to_file_csv([s])
        s = Square(6, 4, 2, 9)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue(len(f.read()) == 41)

    def test_save_to_file_csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as f:
            self.assertEqual("", f.read())

    def test_save_to_file_csv_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("", f.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv_method of Base class."""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(5, 2, 8, 7, 10)
        Rectangle.save_to_file_csv([r1])
        r2 = Rectangle.load_from_file_csv()[0]
        self.assertEqual("[Rectangle] (10) 7/10 - 5/2", str(r2))

    def test_load_from_file_csv_first_square(self):
        s1 = Square(3, 4, 2, 6)
        Square.save_to_file_csv([s1])
        s2 = Square.load_from_file_csv()[0]
        self.assertEqual("[Square] (6) 4/2 - 3", str(s2))

    def test_load_from_file_csv_two_rectangles(self):
        r1 = Rectangle(5, 2, 8, 7, 10)
        r2 = Rectangle(3, 7, 1, 1, 11)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual("[Rectangle] (10) 7/10 - 5/2", str(list_rectangles[0]))
        self.assertEqual("[Rectangle] (11) 1/1 - 3/7", str(list_rectangles[1]))

    def test_load_from_file_csv_two_squares(self):
        s1 = Square(3, 4, 2, 6)
        s2 = Square(8, 2, 1, 7)
        Square.save_to_file_csv([s1, s2])
        list_squares = Square.load_from_file_csv()
        self.assertEqual("[Square] (6) 4/2 - 3", str(_squares[0]))
        self.assertEqual("[Square] (7) 2/1 - 8", str(_squares[1]))

    def test_load_from_file_csv_empty_file(self):
        with open("Rectangle.csv", "w") as f:
            f.write("")
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual([], list_rectangles)

    def test_load_from_file_csv_no_file(self):
        list_rectangles = Rectangle.load_from_file_csv()
        self.assertEqual([], list_rectangles)

    def test_load_from_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv()

    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Square.load_from_file_csv([])


if __name__ == "__main__":
    unittest.main()

