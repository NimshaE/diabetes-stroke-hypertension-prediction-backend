import { shallowMount } from '@vue/test-utils';
import Login from '../Login.vue';

describe('Login.vue', () => {
  it('renders correctly', () => {
    const wrapper = shallowMount(Login);
    expect(wrapper.exists()).toBe(true);
  });

  it('submits the form', async () => {
    const wrapper = shallowMount(Login, {
      data() {
        return {
          username: 'Nimsha',
          password: 'Nish123456',
        };
      },
    });
    const mockPost = jest.fn(() => Promise.resolve({ data: { auth_token: 'mockToken' } }));
    wrapper.vm.$axios.post = mockPost;
    await wrapper.vm.submitForm();
    expect(mockPost).toHaveBeenCalledWith('/api/v1/token/login/', {
      username: 'Nimsha',
      password: 'Nish123456',
    });
    expect(wrapper.vm.$store.state.token).toBe('mockToken');
    expect(localStorage.getItem('token')).toBe('mockToken');

    expect(wrapper.vm.$router.currentRoute.value.path).toBe('/prediction');
  });
});
