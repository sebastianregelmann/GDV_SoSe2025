# Tutorial #10
# ------------
#
# Doing the Fourier Transform for images and back. This code is based on the stackoverflow answer from Fred Weinhaus:
# https://stackoverflow.com/a/59995542

import cv2
import numpy as np

# Global helper variables
window_width = 640
window_height = 480

# TODO Implement the function get_frequencies(image):
def get_frequencies(image):
    # Convert image to floats 
    image_f = np.float32(image)
    # do dft saving as complex output
    dft = cv2.dft(image_f, flags=cv2.DFT_COMPLEX_OUTPUT)
    
    # Apply shift of origin from upper left corner to center of image
    dft_shift = np.fft.fftshift(dft)


    # Extract magnitude and phase images
    mag, phase = cv2.cartToPolar(dft_shift[:, :, 0], dft_shift[:, :, 1])
    # Get spectrum for viewing only
    spec = (1 / 20) * np.log(mag)
    # Return the resulting image (as well as the magnitude and phase for the inverse)
    return spec, dft_shift


# TODO Implement the function create_from_spectrum():
def create_from_spectrum(spectrum_image, dft_shifted):
    
    mag_reconstructed = np.exp(20 * spectrum_image)
    #get real and imageninarey values
    real = dft_shifted[:, :, 0]
    imag = dft_shifted[:, :, 1]
    
    _, phase = cv2.cartToPolar(real, imag)

    # Reconstruct real and imaginary parts from new magnitude and original phase
    real_reconstructed, imag_reconstructed = cv2.polarToCart(mag_reconstructed, phase)
    
        # Merge real and imag channels
    dft_combined = cv2.merge([real_reconstructed, imag_reconstructed])
        # Inverse shift (bring origin back)
    dft_ishift = np.fft.ifftshift(dft_combined)
        # Inverse DFT to get back the image
    img_back = cv2.idft(dft_ishift)
    
    # Get real part
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    # Normalize to 0-255 range and return
    img_back = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX)
    img_back = np.uint8(img_back)
    
    return img_back


def mainipulate_spec(spec):
    # Center coordinates
    #spec = cv2.bitwise_not(spec)
    

    mask = np.zeros(spec.shape, dtype=np.uint8)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cross_width = 5

    # Fill horizontal bar
    mask[cy - cross_width // 2 : cy + cross_width // 2 + 1, :] = 255

    # Fill vertical bar 
    mask[:, cx - cross_width // 2 : cx + cross_width // 2 + 1] = 255

    # Fill horizontal bar of the cross
    mask[cy - 5 // 2 : cy + 5 // 2 + 1, :] = 255

    # Fill vertical bar of the cross
    mask[:, cx -5 // 2 : cx +5 // 2 + 1] = 255
    
    # Add diagonal lines (top-left to bottom-right and top-right to bottom-left)
    line_thickness = cross_width

    # Top-left to bottom-right
    cv2.line(mask, (0, 0), (mask.shape[1]-1, mask.shape[0]-1), color=255, thickness=line_thickness)

    # Top-right to bottom-left
    cv2.line(mask, (mask.shape[1]-1, 0), (0, mask.shape[0]-1), color=255, thickness=line_thickness)

    
    spec = cv2.bitwise_and(spec,spec, mask=mask)
    #spect[0:, 0:int(window_width/2)] = [0,0,0]
    #cv2.circle(spec, (320, 240), 80, (255,255,255), 50)
    
    cv2.imshow("mainpulated spec", spec)
    return spec



# We use a main function this time: see https://realpython.com/python-main-function/ why it makes sense
def main():
    # Load an image, compute frequency domain image from it and display both or vice versa
    image_name = "./tutorials/data/images/chessboard-contrast-squares.jpg"

    # Load the image.
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (window_width, window_height))

    # Show the original image
    # Note that window parameters have no effect on MacOS
    title_original = "Original image"
    cv2.namedWindow(title_original, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_original, window_width, window_height)
    cv2.imshow(title_original, image)

    # result = get_frequencies(image)
    result, dft_shifted  = get_frequencies(image)
    
    # Show the resulting image
    # Note that window parameters have no effect on MacOS
    title_result = "Frequencies image"
    cv2.namedWindow(title_result, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_result, window_width, window_height)
    cv2.imshow(title_result, result)
    
    
    result = mainipulate_spec(result)
    back = create_from_spectrum(result, dft_shifted)
   

    # And compute image back from frequencies
    # Note that window parameters have no effect on MacOS
    title_back = "Reconstructed image"
    cv2.namedWindow(title_back, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_back, window_width, window_height)
    cv2.imshow(title_back, back)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()


# Starting the main function
if __name__ == "__main__":
    main()
