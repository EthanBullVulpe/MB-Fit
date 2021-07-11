# external package imports
import math
from random import Random

class Quaternion(object):
    """
    Quaternion mathmatical object, with one real part and 3 imaginary parts.

    Can be used to perform rotations in 3d space.
    """

    @staticmethod
    def get_random_quaternion(random = Random()):
        """
        Gets a random unit Quaternion.

        Rotations generated by Quaternions produced by this method are NOT gauranteed to be randomly distributed.

        Args:
            random          - The random object used to generate this quaternion. Default is a new Random with a random
                    seed.

        Returns:
            A new random normalized Quaternion.
        """

        return Quaternion(0.5 - random.random(), 0.5 - random.random(), 0.5 - random.random(), 0.5 - random.random()).normalize()

    @staticmethod
    def get_random_rotation_quaternion(random = Random()):
        """
        Gets a random unit Quaternion such that the rotation created by this unit Quaternion is just as likely as any
        other rotation.

        Algorithm is taken from http://planning.cs.uiuc.edu/node198.html.

        Args:
            random          - The random object used to generate this quaternion. Default is a new Random with a random
                    seed.

        Returns:
            A new evenly distributed unit rotation Quaternion.
        """

        X0 = random.random()
        X1 = random.random()
        X2 = random.random()

        t1 = 2 * math.pi * X1
        t2 = 2 * math.pi * X2

        c1 = math.cos(t1)
        s1 = math.sin(t1)
        c2 = math.cos(t2)
        s2 = math.sin(t2)

        r1 = math.sqrt(1 - X0)
        r2 = math.sqrt(X0)

        r = r2*c2
        i = r1*s1
        j = r1*c1
        k = r2*s2

        # now create the Quaternion of rotation
        return Quaternion(r, i, j, k)
    
    def __init__(self, r, i, j, k):
        """
        Creates a new Quaternion from the given real component (r) and 3 imaginary components (i, j, k).

        Args:
            r               - The real component.
            i               - The first imaginary component.
            j               - The second imaginary component.
            k               - The third imaginary component.

        Returns:
            A new Quaternion.
        """

        self.r = r
        self.i = i
        self.j = j
        self.k = k

    def get_r(self):
        """
        Gets the real component of this Quaternion.

        Args:
            None.

        Returns:
            The real component of this Quaternion.
        """

        return self.r

    def get_i(self):
        """
        Gets the first imaginary component of this Quaternion.

        Args:
            None.

        Returns:
            The first imaginary component of this Quaternion.
        """

        return self.i

    def get_j(self):
        """
        Gets the second imaginary component of this Quaternion.

        Args:
            None.

        Returns:
            The second imaginary component of this Quaternion.
        """

        return self.j

    def get_k(self):
        """
        Gets the third imaginary component of this Quaternion.

        Args:
            None.

        Returns:
            The third imaginary component of this Quaternion.
        """

        return self.k

    def __add__(self, other):
        """
        Defines addition of Quaternions as adding each of their components.

        Args:
            other           - The other Quaternion to add to this one.

        Returns:
            The sum of the two Quaternions as a new Quaternion with components equal to the sum of the components in
            this Quaternion and the other.
        """

        return Quaternion(self.r + other.r, self.i + other.i, self.j + other.j, self.k + other.k)

    def __sub__(self, other):
        """
        Defines subtraction of Quaternions as subtracting each of their components.

        Args:
            other           - The other Quaternion to subtract from this one.

        Returns:
            The difference of two Quaternions as a new Quaternion with components equal to that of this Quaternion
            minus those of the other Quaternion.
        """
        return Quaternion(self.r - other.r, self.i - other.i, self.j - other.j, self.k - other.k)

    def __mul__(self, other):
        """
        Defines the product of Quaternions as *magic*.

        Note: multiplication of Quaternions is non-commutative.

        Args:
            other           - The other Quaternion to multiply with this one.

        Returns:
            A new Quaternion that is the product of this one and the other.
        """

        return Quaternion(
            self.r * other.r - self.i * other.i - self.j * other.j - self.k * other.k,
            self.r * other.i + self.i * other.r + self.j * other.k - self.k * other.j,
            self.r * other.j - self.i * other.k + self.j * other.r + self.k * other.i,
            self.r * other.k + self.i * other.j - self.j * other.i + self.k * other.r
        )

    def __abs__(self):
        """
        Defines the absolute value of a Quaternion as its length.

        Args:
            None.

        Returns:
            The length of this Quaternion.
        """

        return math.sqrt(self.r ** 2 + self.i ** 2 + self.j ** 2 + self.k ** 2)

    def __neg__(self):
        """
        Defines the negation of a Quaternion as the negation of each of its components.

        Args:
            None.

        Returns:
            A new Quaternion with components equal to the negated components of this Quaternion.
        """

        return Quaternion(-self.r, -self.i, -self.j, -self.k)

    def __pos__(self):
        """
        Defines the posation of a Quaternion as a clone.

        Args:
            None.

        Returns:
            A new Quaternion with components identical to this Quaternion.
        """
        return Quaternion(+self.r, +self.i, +self.j, +self.k)

    def __eq__(self, other):
        """
        Defines Quaternion equivelence as equivelence of all components.

        Args:
            other           - the Quaternion to compare to this one.

        Returns:
            True if these Quaternions have identical components. False otherwise.
        """

        return self.r == other.r and self.i == other.i and self.j == other.j and self.k == other.k

    def __ne__(self, other):
        """
        Defines Quaternion non-equivelence as non-equivelence of any components.

        Args:
            other           - The Quaternion to compare to this one.

        Returns:
            True if these Quaternions are have any different components. False otherwise.
        """

        return self.r != other.r or self.i != other.i or self.j != other.j or self.k != other.k

    def normalize(self):
        """
        Creates a new unit Quaternion by normalizing this one

        Args:
            None.

        Returns:
            A new Quaternion that is the normalized version of this one.
        """

        length = abs(self)
        return Quaternion(self.r / length, self.i / length, self.j / length, self.k / length)

    def conjugate(self):
        """
        Creates a new Quaternion that is the complex conjugate of this one.

        The product of a Quaternion and its conjugate is a real number (i, j, k are all 0).

        Args:
            None.

        Returns:
            This Quaternion's complex conjugate.
        """

        return Quaternion(self.r, -self.i, -self.j, -self.k)

    def rotate(self, x, y, z, origin_x = 0, origin_y = 0, origin_z = 0):
        """
        Rotates a point in space by the rotation defined by this Quaternion

        Args:
            x               - The x of the point to rotate.
            y               - The y of the point to rotate.
            z               - The z of the point to rotate.
            origin_x        - The x of the point to rotate about.
            origin_y        - The y of the point to rotate about.
            origin_z        - The z of the point to rotate about.

        Returns:
            x, y, z as defined by the input coordinates rotated around the input origin by the rotation defined by this
            Quaternion.
        """

        vector_quaternion = Quaternion(0, x - origin_x, y - origin_y, z - origin_z)

        rotated_quaternion = self * vector_quaternion * self.conjugate()

        x = rotated_quaternion.i + origin_x
        y = rotated_quaternion.j + origin_y
        z = rotated_quaternion.k + origin_z

        return x, y, z